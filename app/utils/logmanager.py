from app import app

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from time import strftime
from flask import Flask, render_template, request

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/affluents.log', maxBytes=10240,
                                       backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')


def logit():
    handler = RotatingFileHandler(app.config['LOGFILE'], maxBytes=10000, backupCount=1)
    handler.setLevel(app.config['LOGGING_LEVEL'])
    app.logger.addHandler(handler)


def logTrace(code_info="missing code information", exc_info="user log info missing"):
    app.logger.error(
        """
--------------------------------------------------------------------
Date :     {dt}
Request:   {method} {path}
IP:        {ip}
User:      {user}
Agent:     {agent_platform} | {agent_browser} {agent_browser_version}
Raw Agent: {agent}
Code Info: {code_info}

            """.format(
            dt=strftime('[%Y-%b-%d %H:%M]'),
            method=request.method,
            path=request.path,
            ip=request.remote_addr,
            agent_platform=request.user_agent.platform,
            agent_browser=request.user_agent.browser,
            agent_browser_version=request.user_agent.version,
            agent=request.user_agent.string,
            user="tdb",
            code_info=code_info
        ), exc_info=exc_info
    )


@app.errorhandler(405)
def page_not_found(error):
    logTrace('Error 404')
    return render_template('404.html'), 404


@app.errorhandler(404)
def page_not_found(error):
    logTrace('Error 404')
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    logTrace('Error 500')
    return render_template('500.html'), 500
