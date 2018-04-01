#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import flask_sqlalchemy
from sqlalchemy import Column,Integer,Sequence, String
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import lib.master

# basedir = os.path.abspath(os.path.dirname(__file__))
# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'DBDOM.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# print(app.config['SQLALCHEMY_DATABASE_URI'])
# db = SQLAlchemy(app)

# class master(db.Model):
#     __tablename__ = 'Master'
#     IDMASTER = db.Column(Integer, primary_key = True)
#     SHOTNAMEMASTER = db.Column(String(200), index = True)
#     FULLNAMEMASTER = db.Column(String(200), index = True)
#     BIRTHDAY = db.Column(String(200), index = True)
#     BIRTHPLACE = db.Column(String(200), index = True)
#     ADRESSREGISTR = db.Column(String(200), index = True)
#     DATARAB = db.Column(String(200), index = True)
#     DATAUVOLN = db.Column(String(200), index = True)
#     NOTES = db.Column(String(200), index = True)
#     PRIZNUVOLN = db.Column(String(200), index = True)
#     PRICHINAUV = db.Column(String(200), index = True)
#     TELEFON = db.Column(String(200), index = True)
#     FOTO = db.Column(String(200), index = True)
#     login = db.Column(String(200), index = True)
#     password = db.Column(String(200), index = True)
#     hash = db.Column(String(200), index = True)
#     def __init__(self, IDMASTER = None,
#                  SHOTNAMEMASTER = None,
#                  FULLNAMEMASTER = None,
#                  BIRTHDAY = None,
#                  BIRTHPLACE = None,
#                  ADRESSREGISTR = None,
#                  DATARAB = None,
#                  DATAUVOLN = None,
#                  NOTES = None,
#                  PRIZNUVOLN = None,
#                  PRICHINAUV = None,
#                  TELEFON = None,
#                  FOTO = None,
#                  login = None,
#                  password = None,
#                  hash = None):
#
#         self.IDMASTER       = IDMASTER
#         self.SHOTNAMEMASTER = SHOTNAMEMASTER
#         self.FULLNAMEMASTER = FULLNAMEMASTER
#         self.BIRTHDAY       = BIRTHDAY
#         self.BIRTHPLACE     = BIRTHPLACE
#         self.ADRESSREGISTR  = ADRESSREGISTR
#         self.DATARAB        = DATARAB
#         self.DATAUVOLN      = DATAUVOLN
#         self.NOTES          = NOTES
#         self.PRIZNUVOLN     = PRIZNUVOLN
#         self.PRICHINAUV     = PRICHINAUV
#         self.TELEFON        = TELEFON
#         self.FOTO           = FOTO
#         self.login          = login
#         self.password       = password
#         self.hash           = hash

# m = lib.master.query.all()#все записи
# mID = master.query.filter_by(IDMASTER=25).first()

import app
from app import db

# m = app.models.Master.query.all()
# for i in m:
#     print(i)
# print("start")

#обновление
# update = app.models.Master.query.filter_by(IDMASTER=25).first()
# update.SHOTNAMEMASTER = "superman"
# db.session.commit()

# добавлине
# mtest = app.models.Master().getValueJson()[1]
# db.session.add(mtest)
# db.session.commit()
# print(mtest)

# удаление
# delete = app.models.Master.query.filter_by(IDMASTER=25).first()
# db.session.delete(delete)
# db.session.commit()

#создание базы
db.create_all()
db.session.commit()

# m = app.models.Master.query.all()
# for i in m:
#     print(i)
# print("end")

import hashlib
LOGIN = "1"
PASSWORD = "1"
h = "кощая задница пушиста {0}{1}".format(LOGIN, PASSWORD)
hx = hashlib.md5()
hx.update(h.encode("utf-8"))
print(h)
print(hx.hexdigest())