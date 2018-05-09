#!/usr/bin/python3
# -*- coding: utf-8 -*-

from flask import Flask, session, redirect, url_for, escape, request, jsonify, g, abort, flash, url_for, render_template
from sqlalchemy.exc import IntegrityError
from flask import request
from app.models import Master, Static, Declaration
from app import db
from app import app
import datetime
import json
import hashlib

import lib.master
import lib.SQLConnect
# app = Flask(__name__)
# app.config['JSON_AS_ASCII'] = False
MD5 = "d55561f495b46e262733602ae825465d"
def setStatic(staticlist):
    for i in staticlist:
        try:
            i.write = "True"
            db.session.add(i)
            db.session.commit()
        except IntegrityError:
            print("Error setStatic")
            i.write = "False"

class JSONEncoder(app.json_encoder):
    def default(self, o):
        if hasattr(o, 'as_json'):
            return o.as_json()
        else:
            return super().default(o)

app.json_encoder = JSONEncoder

@app.route('/master/<USERNAME>/add/list/{0}'.format(MD5), methods=['GET', 'POST'])
def addMasters(USERNAME):
    statics = []
    try:
        data = request.data
        masters = Master.loadJson(data)
        for mas in masters:
            try:
                db.session.add(mas)
                db.session.commit()
                stat = Static(idUser=USERNAME,
                              nameTable="Master",
                              IdTable=mas.IDMASTER,
                              operator="add",
                              success="True",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=mas.__str__())
                statics.append(stat)
            except IntegrityError as ex:
                db.session.rollback()
                stat = Static(idUser=USERNAME,
                              nameTable="Master",
                              IdTable=0,
                              operator="add",
                              success="False",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=ex.__str__(),
                              error="IntegrityError/Add")
                statics.append(stat)
                print("error add: \n {}".format(ex.__str__()))
        setStatic(statics)
        return jsonify(statics)
    except Exception as ex:
        stat = Static(idUser=USERNAME,
                      nameTable="Master",
                      IdTable=0,
                      operator="add",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="request.data/Master.loadJson(data)")
        statics.append(stat)
        setStatic(statics)
        return jsonify(statics)

@app.route('/servis/getmd5/<usermd5>', methods=['GET', 'POST'])
def getmd5(usermd5):
    try:
        if usermd5 == MD5:
            return "1"
        else:
            return "2"
    except Exception as ex:
        return "3"

@app.route('/master/<USERNAME>/dell/list/{0}'.format(MD5), methods=['GET', 'POST'])
def dellMasters(USERNAME):
    statics = []
    try:
        data = request.data
        masters = Master.loadJson(data)
        for mas in masters:
            try:
                delete = Master.query.filter_by(IDMASTER=mas.IDMASTER).first()
                db.session.delete(delete)
                db.session.commit()
                stat = Static(idUser=USERNAME,
                              nameTable="Master",
                              IdTable=mas.IDMASTER,
                              operator="delete",
                              success="True",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=mas.__str__())
                statics.append(stat)
            except IntegrityError as ex:
                db.session.rollback()
                stat = Static(idUser=USERNAME,
                              nameTable="Master",
                              IdTable=0,
                              operator="delete",
                              success="False",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=ex.__str__(),
                              error="IntegrityError/delete")
                statics.append(stat)
                print("error add: \n {}".format(ex.__str__()))
        setStatic(statics)
        return jsonify(statics)
    except Exception as ex:
        stat = Static(idUser=USERNAME,
                      nameTable="Master",
                      IdTable=0,
                      operator="delete",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="request.data/Master.loadJson(data)")
        statics.append(stat)
        setStatic(statics)
        return jsonify(statics)

@app.route('/master/<USERNAME>/get/list/{0}'.format(MD5), methods=['GET', 'POST'])
def getMasters(USERNAME):
    statics = []
    text = '[]'
    try:
        masters = Master.query.all()

        if masters == None or masters == []:
            masters = "{}"
            text = "[]"
        else:
            text = masters.__str__()
        stat = Static(idUser=USERNAME,
                      nameTable="Master",
                      IdTable=0,
                      operator="get",
                      success="True",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=text,
                      error="")
        statics.append(stat)
        setStatic(statics)
        return jsonify(masters)
    except IntegrityError as ex:
        stat = Static(idUser=USERNAME,
                      nameTable="Master",
                      IdTable=0,
                      operator="get",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="app.models.Master.query.all()")
        statics.append(stat)
        setStatic(statics)
        return jsonify("{}")

@app.route('/declaration/<USERNAME>/add/list/{0}'.format(MD5), methods=['GET', 'POST'])
def addDeclarations(USERNAME):
    statics = []
    try:
        data = request.data
        declarations = Declaration.loadJson(data)
        for dec in declarations:
            try:
                db.session.add(dec)
                db.session.commit()
                stat = Static(idUser=USERNAME,
                              nameTable="Declaration",
                              IdTable=dec.DECLID,
                              operator="add",
                              success="True",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=dec.__str__())
                statics.append(stat)
            except IntegrityError as ex:
                db.session.rollback()
                stat = Static(idUser=USERNAME,
                              nameTable="Declaration",
                              IdTable=0,
                              operator="add",
                              success="False",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=ex.__str__(),
                              error="IntegrityError/Add")
                statics.append(stat)
                print("error add: \n {}".format(ex.__str__()))
        setStatic(statics)
        return jsonify(statics)
    except Exception as ex:
        stat = Static(idUser=USERNAME,
                      nameTable="Declaration",
                      IdTable=0,
                      operator="add",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="request.data/Declaration.loadJson(data)")
        statics.append(stat)
        setStatic(statics)
        return jsonify(statics)

@app.route('/declaration/<USERNAME>/dell/list/{0}'.format(MD5), methods=['GET', 'POST'])
def dellDeclarations(USERNAME):
    statics = []
    try:
        data = request.data
        declarations = Declaration.loadJson(data)
        for dec in declarations:
            try:
                delete = Declaration.query.filter_by(DECLID=dec.DECLID).first()
                db.session.delete(delete)
                db.session.commit()
                stat = Static(idUser=USERNAME,
                              nameTable="Declaration",
                              IdTable=dec.DECLID,
                              operator="delete",
                              success="True",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=dec.__str__())
                statics.append(stat)
            except IntegrityError as ex:
                db.session.rollback()
                stat = Static(idUser=USERNAME,
                              nameTable="Declaration",
                              IdTable=0,
                              operator="delete",
                              success="False",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=ex.__str__(),
                              error="IntegrityError/delete")
                statics.append(stat)
                print("error add: \n {}".format(ex.__str__()))
        setStatic(statics)
        return jsonify(statics)
    except Exception as ex:
        stat = Static(idUser=USERNAME,
                      nameTable="Declaration",
                      IdTable=0,
                      operator="delete",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="request.data/Declaration.loadJson(data)")
        statics.append(stat)
        setStatic(statics)
        return jsonify(statics)

@app.route('/declaration/<USERNAME>/get/list/{0}'.format(MD5), methods=['GET', 'POST'])
def getDeclarations(USERNAME):
    statics = []
    text = '[]'
    try:
        declarations = Declaration.query.all()

        if declarations == None or declarations == []:
            declarations = "{}"
            text = "[]"
        else:
            text = declarations.__str__()

        stat = Static(idUser=USERNAME,
                      nameTable="Declaration",
                      IdTable=0,
                      operator="get",
                      success="True",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=text,
                      error="")
        statics.append(stat)
        setStatic(statics)
        return jsonify(declarations)
    except Exception as ex:
        stat = Static(idUser=USERNAME,
                      nameTable="Declaration",
                      IdTable=0,
                      operator="get",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="request.data/Declaration.loadJson(data)")
        statics.append(stat)
        setStatic(statics)
        return jsonify("{}")

@app.route('/Android/<HASH>/get/declarations/list/{0}'.format(MD5), methods=['GET', 'POST'])
def getAndroid(HASH):
    statics = []
    text = '[]'
    try:
        user = Master.query.filter_by(HASH=HASH).first()

        if user == None and user == []:
            return

        declarations = Declaration.query.filter_by(MASTERID=user.IDMASTER).all()

        if declarations == None or declarations == []:
            declarations = "{}"
            text = "[]"
        else:
            text = declarations.__str__()

        stat = Static(idUser=HASH,
                      nameTable="Declaration",
                      IdTable=0,
                      operator="get",
                      success="True",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=text,
                      error="")
        statics.append(stat)
        setStatic(statics)
        return jsonify(declarations)
    except Exception as ex:
        stat = Static(idUser=HASH,
                      nameTable="Declaration",
                      IdTable=0,
                      operator="get",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="")
        statics.append(stat)
        setStatic(statics)
        return "null"

@app.route('/Android/<HASH>/update/declarations/list/{0}'.format(MD5), methods=['GET', 'POST'])
def updateAndroid(HASH):
    statics = []

    user = Master.query.filter_by(HASH=HASH).first()

    if user == None and user == []:
        return

    try:
        data = request.data
        declarations = Declaration.loadJson(data)
        for dec in declarations:
            try:
                db.session.add(dec)
                db.session.commit()
                stat = Static(idUser=HASH,
                              nameTable="Declaration",
                              IdTable=dec.DECLID,
                              operator="add",
                              success="True",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=dec.__str__())
                statics.append(stat)
            except IntegrityError as ex:
                db.session.rollback()
                stat = Static(idUser=HASH,
                              nameTable="Declaration",
                              IdTable=0,
                              operator="add",
                              success="False",
                              dateUpdate=datetime.datetime.utcnow().__str__(),
                              text=ex.__str__(),
                              error="IntegrityError/Add")
                statics.append(stat)
                print("error add: \n {}".format(ex.__str__()))
        setStatic(statics)
        return jsonify(statics)
    except Exception as ex:
        stat = Static(idUser=HASH,
                      nameTable="Declaration",
                      IdTable=0,
                      operator="add",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="request.data/Declaration.loadJson(data)")
        statics.append(stat)
        setStatic(statics)
        return jsonify(statics)

@app.route('/masterpasword/<USERNAME>/<LOGIN>/<PASSWORD>/<IDMASTER>/setpassword/item/{0}'.format(MD5), methods=['GET', 'POST'])
def setPassword(USERNAME, LOGIN, PASSWORD, IDMASTER):
    statics = []
    try:

        user = Master.query.filter_by(IDMASTER=IDMASTER).first()

        if(user != None):
            user.login = LOGIN
            user.password = PASSWORD

            h = "кощая задница пушиста {0}{1}".format(LOGIN, PASSWORD)
            hx = hashlib.md5()
            hx.update(h.encode("utf-8"))
            user.HASH = hx.hexdigest()
            db.session.commit()

            stat = Static(idUser=USERNAME,
                          nameTable="Master",
                          IdTable=user.IDMASTER,
                          operator="setpassword",
                          success="True",
                          dateUpdate=datetime.datetime.utcnow().__str__(),
                          text=user.__str__(),
                          error="")
            statics.append(stat)
            setStatic(statics)

    except Exception as ex:
        stat = Static(idUser=USERNAME,
                      nameTable="Master",
                      IdTable=0,
                      operator="setpassword",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="hashlib.md5")
        statics.append(stat)
        setStatic(statics)

    return jsonify(statics)

@app.route('/Android/<LOGIN>/<PASSWORD>/getHASH/item/{0}'.format(MD5), methods=['GET', 'POST'])
def getPassword(LOGIN, PASSWORD):
    statics = []
    user = None
    try:

        if(LOGIN != "" and LOGIN != None and PASSWORD != "" and PASSWORD != None):
            user = Master.query.filter_by(login=LOGIN, password=PASSWORD).first()

        if(user != None):

            stat = Static(idUser="GetHASH",
                          nameTable="Master",
                          IdTable=user.IDMASTER,
                          operator="Android/getHASH",
                          success="True",
                          dateUpdate=datetime.datetime.utcnow().__str__(),
                          text=user.__str__(),
                          error="")
            statics.append(stat)
            setStatic(statics)
            return user.HASH;
        else:
            stat = Static(idUser="GetHASH",
                          nameTable="Master",
                          IdTable=0,
                          operator="Android/getHASH",
                          success="False",
                          dateUpdate=datetime.datetime.utcnow().__str__(),
                          text="error login, password",
                          error="user == None, LOGIN/PASSWORD")
            statics.append(stat)
            setStatic(statics)
            return "error login, password"

    except Exception as ex:
        stat = Static(idUser="GetHASH",
                      nameTable="Master",
                      IdTable=0,
                      operator="Android/getHASH",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="user.HASH")
        statics.append(stat)
        setStatic(statics)
    return "error"

@app.route('/Android/<HASH>/<DECLID>/<int:SOSTZAKAZID>/setSOSTZAKAZID/item/{0}'.format(MD5), methods=['GET', 'POST'])
def setSOSTZAKAZID(HASH, DECLID, SOSTZAKAZID):
    statics = []
    try:
        user = Master.query.filter_by(HASH=HASH).first()

        if user == None and user == []:
            return

        declarations = Declaration.query.filter_by(DECLID=DECLID).all()

        for i in declarations:
            i.SOSTZAKAZID = int(SOSTZAKAZID)
            db.session.commit()
            stat = Static(idUser=HASH,
                          nameTable="Declaration",
                          IdTable=user.IDMASTER,
                          operator="setSOSTZAKAZID",
                          success="True",
                          dateUpdate=datetime.datetime.utcnow().__str__(),
                          text=user.__str__(),
                          error="")
            statics.append(stat)
            setStatic(statics)

        if declarations != None and declarations != []:
            return "true"
        else:

            stat = Static(idUser=HASH,
                          nameTable="Declaration",
                          IdTable=user.IDMASTER,
                          operator="setSOSTZAKAZID",
                          success="False",
                          dateUpdate=datetime.datetime.utcnow().__str__(),
                          text="not Declaration: {0}".format(DECLID),
                          error="")
            statics.append(stat)
            setStatic(statics)

            return "false"

    except Exception as ex:
        stat = Static(idUser=HASH,
                      nameTable="Declaration",
                      IdTable=user.IDMASTER,
                      operator="setSOSTZAKAZID",
                      success="False",
                      dateUpdate=datetime.datetime.utcnow().__str__(),
                      text=ex.__str__(),
                      error="")
        statics.append(stat)
        setStatic(statics)
        return "error"

if __name__ == "__main__":
    app.run(debug=True)