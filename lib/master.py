#!/usr/bin/python3
# -*- coding: utf-8 -*-
import json
import lib.SQLConnect
import flask_sqlalchemy
from sqlalchemy import Column,Integer,Sequence, String

Base = flask_sqlalchemy.declarative_base()
#class master(Base):
class master(Base):
    __tablename__ = 'Master'
    IDMASTER = Column(Integer, primary_key = True)
    SHOTNAMEMASTER = Column(String(200), index = True)
    FULLNAMEMASTER = Column(String(200), index = True)
    BIRTHDAY = Column(String(200), index = True)
    BIRTHPLACE = Column(String(200), index = True)
    ADRESSREGISTR = Column(String(200), index = True)
    DATARAB = Column(String(200), index = True)
    DATAUVOLN = Column(String(200), index = True)
    NOTES = Column(String(200), index = True)
    PRIZNUVOLN = Column(String(200), index = True)
    PRICHINAUV = Column(String(200), index = True)
    TELEFON = Column(String(200), index = True)
    FOTO = Column(String(200), index = True)
    login = Column(String(200), index = True)
    password = Column(String(200), index = True)
    hash = Column(String(200), index = True)
    def __init__(self, IDMASTER = None,
                 SHOTNAMEMASTER = None,
                 FULLNAMEMASTER = None,
                 BIRTHDAY = None,
                 BIRTHPLACE = None,
                 ADRESSREGISTR = None,
                 DATARAB = None,
                 DATAUVOLN = None,
                 NOTES = None,
                 PRIZNUVOLN = None,
                 PRICHINAUV = None,
                 TELEFON = None,
                 FOTO = None,
                 login = None,
                 password = None,
                 hash = None):

        self.IDMASTER       = IDMASTER
        self.SHOTNAMEMASTER = SHOTNAMEMASTER
        self.FULLNAMEMASTER = FULLNAMEMASTER
        self.BIRTHDAY       = BIRTHDAY
        self.BIRTHPLACE     = BIRTHPLACE
        self.ADRESSREGISTR  = ADRESSREGISTR
        self.DATARAB        = DATARAB
        self.DATAUVOLN      = DATAUVOLN
        self.NOTES          = NOTES
        self.PRIZNUVOLN     = PRIZNUVOLN
        self.PRICHINAUV     = PRICHINAUV
        self.TELEFON        = TELEFON
        self.FOTO           = FOTO
        self.login          = login
        self.password       = password
        self.hash           = hash

    def decoder(obj):
        return master(
            IDMASTER=obj.get('IDMASTER'),
            SHOTNAMEMASTER=obj.get('SHOTNAMEMASTER'),
            FULLNAMEMASTER=obj.get('FULLNAMEMASTER'),
            BIRTHDAY=obj.get('BIRTHDAY'),
            BIRTHPLACE=obj.get('BIRTHPLACE'),
            ADRESSREGISTR=obj.get('ADRESSREGISTR'),
            DATARAB=obj.get('DATARAB'),
            DATAUVOLN=obj.get('DATAUVOLN'),
            NOTES=obj.get('NOTES'),
            PRIZNUVOLN=obj.get('PRIZNUVOLN'),
            PRICHINAUV=obj.get('PRICHINAUV'),
            TELEFON=obj.get('TELEFON'),
            FOTO=obj.get('FOTO'),
            login=obj.get('login'),
            password=obj.get('password'),
            hash=obj.get('hash'),
        )

    def getValue(self):
        return (self.IDMASTER,
            self.SHOTNAMEMASTER,
            self.FULLNAMEMASTER,
            self.BIRTHDAY,
            self.BIRTHPLACE,
            self.ADRESSREGISTR,
            self.DATARAB,
            self.DATAUVOLN,
            self.NOTES,
            self.PRIZNUVOLN,
            self.PRICHINAUV,
            self.TELEFON,
            self.FOTO,
            self.login,
            self.password,
            self.hash)

    def getValueJson(self):

        j = b'[{"IDMASTER":23,"SHOTNAMEMASTER":"\xd0\x92\xd0\xb8\xd1\x82\xd1\x8f","FULLNAMEMASTER":"\xd0\xa1\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xb8\xd1\x87 \xd0\x92\xd0\xb8\xd0\xba\xd1\x82\xd0\xbe\xd1\x80 \xd0\x90\xd0\xbd\xd0\xb0\xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb5\xd0\xb2\xd0\xb8\xd1\x87","BIRTHDAY":"1970-09-20T00:00:00","BIRTHPLACE":"\xd0\xbf\xd0\xbe\xd1\x81. \xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xb9\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xa8\xd0\xb8\xd0\xbb\xd0\xba\xd0\xb8\xd0\xbd\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x80-\xd0\xbd\xd0\xb0 \xd0\xa7\xd0\xb8\xd1\x82. \xd0\xbe\xd0\xb1\xd0\xbb.","ADRESSREGISTR":"\xd1\x83\xd0\xbb. \xd0\x9a\xd0\xb0\xd0\xb7\xd0\xb0\xd1\x87\xd1\x8c\xd1\x8f 5 \xd0\xba\xd0\xb2.8","ADRESSFACT":"","DATARAB":"2011-01-12T00:00:00","DATAUVOLN":"2011-03-03T00:00:00","NOTES":"","PRIZNUVOLN":1,"PRICHINAUV":"","TELEFON":"8924-275-98-62","FOTO":""},{"IDMASTER":21,"SHOTNAMEMASTER":"\xd0\x92\xd1\x8f\xd1\x87\xd0\xb5\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb2","FULLNAMEMASTER":"\xd0\x9f\xd0\xbe\xd1\x80\xd1\x82\xd0\xbd\xd1\x8f\xd0\xb3\xd0\xb8\xd0\xbd","BIRTHDAY":"1987-03-03T00:00:00","BIRTHPLACE":"","ADRESSREGISTR":"","ADRESSFACT":"","DATARAB":"2010-11-10T00:00:00","DATAUVOLN":"2011-11-02T00:00:00","NOTES":"","PRIZNUVOLN":1,"PRICHINAUV":"","TELEFON":"8924-387-15-10","FOTO":""},{"IDMASTER":22,"SHOTNAMEMASTER":"\xd0\x98\xd0\xb3\xd0\xbe\xd1\x80\xd1\x8c","FULLNAMEMASTER":"\xd0\x9a\xd0\xb8\xd1\x81\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb2","BIRTHDAY":null,"BIRTHPLACE":"","ADRESSREGISTR":"","ADRESSFACT":"","DATARAB":"2011-04-07T00:00:00","DATAUVOLN":"2012-02-27T00:00:00","NOTES":"","PRIZNUVOLN":1,"PRICHINAUV":"\xd0\xbf\xd0\xbe \xd1\x81\xd0\xbe\xd0\xb1\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xbc\xd1\x83 \xd0\xb6\xd0\xb5\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8e","TELEFON":"8914-447-48-40","FOTO":""},{"IDMASTER":24,"SHOTNAMEMASTER":"\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd","FULLNAMEMASTER":"\xd0\xa1\xd0\xb5\xd0\xbb\xd1\x8e\xd0\xba\xd0\xbe\xd0\xb2","BIRTHDAY":"1969-11-10T00:00:00","BIRTHPLACE":"","ADRESSREGISTR":"\xd0\xba\xd1\x81\xd0\xba 6 \xd0\xbc\xd0\xba\xd1\x80 \xd0\xb4.5 \xd0\xba\xd0\xb2 65","ADRESSFACT":"\xd0\xba\xd1\x81\xd0\xba 6 \xd0\xbc\xd0\xba\xd1\x80 \xd0\xb4.19\xd0\xb0 \xd0\xba\xd0\xb2 36","DATARAB":"2011-06-16T00:00:00","DATAUVOLN":null,"NOTES":"","PRIZNUVOLN":0,"PRICHINAUV":"","TELEFON":"8-924-278-2660 / 31-18-60","FOTO":""},{"IDMASTER":25,"SHOTNAMEMASTER":"\xd0\x91\xd0\xb0\xd1\x82\xd0\xbe","FULLNAMEMASTER":"\xd0\xa1\xd1\x8b\xd0\xbd\xd0\xb3\xd0\xb5\xd0\xb5\xd0\xb2 \xd0\x91\xd0\xb0\xd1\x82\xd0\xbe\xd0\xb6\xd0\xb0\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbb \xd0\x93\xd0\xb0\xd1\x80\xd0\xbc\xd0\xb0\xd0\xb5\xd0\xb2\xd0\xb8\xd1\x87","BIRTHDAY":"2019-04-27T00:00:00","BIRTHPLACE":"\xd1\x81.\xd0\x91\xd1\x83\xd0\xbb\xd1\x83\xd0\xbc \xd0\x9e\xd0\xbb\xd0\xbe\xd0\xb2\xd1\x8f\xd0\xbd\xd0\xbd\xd0\xb8\xd0\xbd\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x80\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd\xd0\xb0","ADRESSREGISTR":"\xd0\xbf. \xd0\xaf\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x80\xd1\x81\xd0\xba, \xd0\xa1\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbc\xd0\xba\xd1\x80. \xd0\xb4.4,\xd0\xba\xd0\xb2.20","ADRESSFACT":"\xd0\xb3.\xd0\xaf\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x80\xd1\x81\xd0\xba, \xd0\xbc\xd0\xba\xd1\x80.\xd0\xa1\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb4.4 \xd0\xba\xd0\xb2.20","DATARAB":"2011-10-11T00:00:00","DATAUVOLN":null,"NOTES":"","PRIZNUVOLN":0,"PRICHINAUV":"","TELEFON":"924-374-66-75","FOTO":""},{"IDMASTER":26,"SHOTNAMEMASTER":"\xd0\x9c\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc","FULLNAMEMASTER":"\xd0\xa7\xd1\x83\xd0\xbc\xd0\xb0\xd0\xba \xd0\xbc\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc \xd0\x93\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb0\xd0\xb4\xd1\x8c\xd0\xb5\xd0\xb2\xd0\xb8\xd1\x87","BIRTHDAY":"1984-05-05T00:00:00","BIRTHPLACE":"\xd0\xb3.\xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0","ADRESSREGISTR":"\xd0\x93.\xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0, 2-\xd0\xb0\xd1\x8f \xd0\x9a\xd1\x80\xd0\xb0\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xbd\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd0\xb4.11 \xd0\xba\xd0\xb2.1","ADRESSFACT":"\xd0\x93. \xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0, \xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xbf\xd0\xb5\xd0\xba\xd1\x82 \xd0\xa1\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb2 \xd0\xb4.1 \xd0\xba\xd0\xb2.77","DATARAB":"2012-03-26T00:00:00","DATAUVOLN":null,"NOTES":"","PRIZNUVOLN":0,"PRICHINAUV":"","TELEFON":"914-464-77-28","FOTO":""}]'

        value = json.loads(j.decode("utf-8"), object_hook=master.decoder)
        return  value

    def loadJson(strJson):
        value = []

        try:
            value = json.loads(strJson.decode("utf-8"), object_hook=master.decoder)
        except Exception as ex:
            print("Ошибка загрузки JSON Master {}".format(ex))

        return value

    def __str__(self):
        return "{}, {}, {}".format(self.IDMASTER, self.SHOTNAMEMASTER, self.FULLNAMEMASTER)

    def __repr__(self):
        return "{}, {}, {}".format(self.IDMASTER, self.SHOTNAMEMASTER, self.FULLNAMEMASTER)

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)