from app import db
import json
ROLE_USER = 0
ROLE_ADMIN = 1

class UserMaster(db.Model):
    __tablename__ = 'UserMaster'
    id = db.Column(db.Integer, primary_key = True)
    nickname = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    def __init__(self, id = None, nickname = None, email = None):
        self.id = id
        self.nickname = nickname
        self.email = email

class Master(db.Model):
    __tablename__ = 'Master'
    IDMASTER = db.Column(db.Integer, primary_key = True)
    SHOTNAMEMASTER = db.Column(db.String(200), index = True)
    FULLNAMEMASTER = db.Column(db.String(200), index = True)
    BIRTHDAY = db.Column(db.String(200), index = True)
    BIRTHPLACE = db.Column(db.String(200), index = True)
    ADRESSREGISTR = db.Column(db.String(200), index = True)
    DATARAB = db.Column(db.String(200), index = True)
    DATAUVOLN = db.Column(db.String(200), index = True)
    NOTES = db.Column(db.String(200), index = True)
    PRIZNUVOLN = db.Column(db.String(200), index = True)
    PRICHINAUV = db.Column(db.String(200), index = True)
    TELEFON = db.Column(db.String(200), index = True)
    FOTO = db.Column(db.String(200), index = True)
    login = db.Column(db.String(200), index = True)
    password = db.Column(db.String(200), index = True)
    HASH = db.Column(db.String(200), index = True)

    def __init__(self, IDMASTER=None,
                 SHOTNAMEMASTER=None,
                 FULLNAMEMASTER=None,
                 BIRTHDAY=None,
                 BIRTHPLACE=None,
                 ADRESSREGISTR=None,
                 DATARAB=None,
                 DATAUVOLN=None,
                 NOTES=None,
                 PRIZNUVOLN=None,
                 PRICHINAUV=None,
                 TELEFON=None,
                 FOTO=None,
                 login=None,
                 password=None,
                 HASH=None):

        self.IDMASTER = IDMASTER
        self.SHOTNAMEMASTER = SHOTNAMEMASTER
        self.FULLNAMEMASTER = FULLNAMEMASTER
        self.BIRTHDAY = BIRTHDAY
        self.BIRTHPLACE = BIRTHPLACE
        self.ADRESSREGISTR = ADRESSREGISTR
        self.DATARAB = DATARAB
        self.DATAUVOLN = DATAUVOLN
        self.NOTES = NOTES
        self.PRIZNUVOLN = PRIZNUVOLN
        self.PRICHINAUV = PRICHINAUV
        self.TELEFON = TELEFON
        self.FOTO = FOTO
        self.login = login
        self.password = password
        self.HASH = HASH

    def __repr__(self):
        return "{}, {}, {}".format(self.IDMASTER, self.SHOTNAMEMASTER, self.FULLNAMEMASTER)

    def __str__(self):
        return "{}, {}, {}".format(self.IDMASTER, self.SHOTNAMEMASTER, self.FULLNAMEMASTER)

    def decoder(obj):
        return Master(
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
            HASH=obj.get('HASH'),)

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
                self.HASH)

    def getValueJson(self):

        j = b'[{"IDMASTER":23,"SHOTNAMEMASTER":"\xd0\x92\xd0\xb8\xd1\x82\xd1\x8f","FULLNAMEMASTER":"\xd0\xa1\xd0\xbb\xd0\xbe\xd0\xbd\xd0\xb8\xd1\x87 \xd0\x92\xd0\xb8\xd0\xba\xd1\x82\xd0\xbe\xd1\x80 \xd0\x90\xd0\xbd\xd0\xb0\xd1\x82\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb5\xd0\xb2\xd0\xb8\xd1\x87","BIRTHDAY":"1970-09-20T00:00:00","BIRTHPLACE":"\xd0\xbf\xd0\xbe\xd1\x81. \xd0\x9f\xd0\xb5\xd1\x80\xd0\xb2\xd0\xbe\xd0\xbc\xd0\xb0\xd0\xb9\xd1\x81\xd0\xba\xd0\xb8\xd0\xb9 \xd0\xa8\xd0\xb8\xd0\xbb\xd0\xba\xd0\xb8\xd0\xbd\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x80-\xd0\xbd\xd0\xb0 \xd0\xa7\xd0\xb8\xd1\x82. \xd0\xbe\xd0\xb1\xd0\xbb.","ADRESSREGISTR":"\xd1\x83\xd0\xbb. \xd0\x9a\xd0\xb0\xd0\xb7\xd0\xb0\xd1\x87\xd1\x8c\xd1\x8f 5 \xd0\xba\xd0\xb2.8","ADRESSFACT":"","DATARAB":"2011-01-12T00:00:00","DATAUVOLN":"2011-03-03T00:00:00","NOTES":"","PRIZNUVOLN":1,"PRICHINAUV":"","TELEFON":"8924-275-98-62","FOTO":""},{"IDMASTER":21,"SHOTNAMEMASTER":"\xd0\x92\xd1\x8f\xd1\x87\xd0\xb5\xd1\x81\xd0\xbb\xd0\xb0\xd0\xb2","FULLNAMEMASTER":"\xd0\x9f\xd0\xbe\xd1\x80\xd1\x82\xd0\xbd\xd1\x8f\xd0\xb3\xd0\xb8\xd0\xbd","BIRTHDAY":"1987-03-03T00:00:00","BIRTHPLACE":"","ADRESSREGISTR":"","ADRESSFACT":"","DATARAB":"2010-11-10T00:00:00","DATAUVOLN":"2011-11-02T00:00:00","NOTES":"","PRIZNUVOLN":1,"PRICHINAUV":"","TELEFON":"8924-387-15-10","FOTO":""},{"IDMASTER":22,"SHOTNAMEMASTER":"\xd0\x98\xd0\xb3\xd0\xbe\xd1\x80\xd1\x8c","FULLNAMEMASTER":"\xd0\x9a\xd0\xb8\xd1\x81\xd0\xb5\xd0\xbb\xd0\xb5\xd0\xb2","BIRTHDAY":null,"BIRTHPLACE":"","ADRESSREGISTR":"","ADRESSFACT":"","DATARAB":"2011-04-07T00:00:00","DATAUVOLN":"2012-02-27T00:00:00","NOTES":"","PRIZNUVOLN":1,"PRICHINAUV":"\xd0\xbf\xd0\xbe \xd1\x81\xd0\xbe\xd0\xb1\xd1\x81\xd1\x82\xd0\xb2\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xbe\xd0\xbc\xd1\x83 \xd0\xb6\xd0\xb5\xd0\xbb\xd0\xb0\xd0\xbd\xd0\xb8\xd1\x8e","TELEFON":"8914-447-48-40","FOTO":""},{"IDMASTER":24,"SHOTNAMEMASTER":"\xd0\x98\xd0\xb2\xd0\xb0\xd0\xbd","FULLNAMEMASTER":"\xd0\xa1\xd0\xb5\xd0\xbb\xd1\x8e\xd0\xba\xd0\xbe\xd0\xb2","BIRTHDAY":"1969-11-10T00:00:00","BIRTHPLACE":"","ADRESSREGISTR":"\xd0\xba\xd1\x81\xd0\xba 6 \xd0\xbc\xd0\xba\xd1\x80 \xd0\xb4.5 \xd0\xba\xd0\xb2 65","ADRESSFACT":"\xd0\xba\xd1\x81\xd0\xba 6 \xd0\xbc\xd0\xba\xd1\x80 \xd0\xb4.19\xd0\xb0 \xd0\xba\xd0\xb2 36","DATARAB":"2011-06-16T00:00:00","DATAUVOLN":null,"NOTES":"","PRIZNUVOLN":0,"PRICHINAUV":"","TELEFON":"8-924-278-2660 / 31-18-60","FOTO":""},{"IDMASTER":25,"SHOTNAMEMASTER":"\xd0\x91\xd0\xb0\xd1\x82\xd0\xbe","FULLNAMEMASTER":"\xd0\xa1\xd1\x8b\xd0\xbd\xd0\xb3\xd0\xb5\xd0\xb5\xd0\xb2 \xd0\x91\xd0\xb0\xd1\x82\xd0\xbe\xd0\xb6\xd0\xb0\xd1\x80\xd0\xb3\xd0\xb0\xd0\xbb \xd0\x93\xd0\xb0\xd1\x80\xd0\xbc\xd0\xb0\xd0\xb5\xd0\xb2\xd0\xb8\xd1\x87","BIRTHDAY":"2019-04-27T00:00:00","BIRTHPLACE":"\xd1\x81.\xd0\x91\xd1\x83\xd0\xbb\xd1\x83\xd0\xbc \xd0\x9e\xd0\xbb\xd0\xbe\xd0\xb2\xd1\x8f\xd0\xbd\xd0\xbd\xd0\xb8\xd0\xbd\xd1\x81\xd0\xba\xd0\xbe\xd0\xb3\xd0\xbe \xd1\x80\xd0\xb0\xd0\xb9\xd0\xbe\xd0\xbd\xd0\xb0","ADRESSREGISTR":"\xd0\xbf. \xd0\xaf\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x80\xd1\x81\xd0\xba, \xd0\xa1\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xbc\xd0\xba\xd1\x80. \xd0\xb4.4,\xd0\xba\xd0\xb2.20","ADRESSFACT":"\xd0\xb3.\xd0\xaf\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb3\xd0\xbe\xd1\x80\xd1\x81\xd0\xba, \xd0\xbc\xd0\xba\xd1\x80.\xd0\xa1\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd1\x87\xd0\xbd\xd1\x8b\xd0\xb9 \xd0\xb4.4 \xd0\xba\xd0\xb2.20","DATARAB":"2011-10-11T00:00:00","DATAUVOLN":null,"NOTES":"","PRIZNUVOLN":0,"PRICHINAUV":"","TELEFON":"924-374-66-75","FOTO":""},{"IDMASTER":26,"SHOTNAMEMASTER":"\xd0\x9c\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc","FULLNAMEMASTER":"\xd0\xa7\xd1\x83\xd0\xbc\xd0\xb0\xd0\xba \xd0\xbc\xd0\xb0\xd0\xba\xd1\x81\xd0\xb8\xd0\xbc \xd0\x93\xd0\xb5\xd0\xbd\xd0\xbd\xd0\xb0\xd0\xb4\xd1\x8c\xd0\xb5\xd0\xb2\xd0\xb8\xd1\x87","BIRTHDAY":"1984-05-05T00:00:00","BIRTHPLACE":"\xd0\xb3.\xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0","ADRESSREGISTR":"\xd0\x93.\xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0, 2-\xd0\xb0\xd1\x8f \xd0\x9a\xd1\x80\xd0\xb0\xd1\x81\xd0\xbd\xd0\xbe\xd0\xb4\xd0\xbe\xd0\xbd\xd1\x81\xd0\xba\xd0\xb0\xd1\x8f \xd0\xb4.11 \xd0\xba\xd0\xb2.1","ADRESSFACT":"\xd0\x93. \xd0\xa7\xd0\xb8\xd1\x82\xd0\xb0, \xd0\xbf\xd1\x80\xd0\xbe\xd1\x81\xd0\xbf\xd0\xb5\xd0\xba\xd1\x82 \xd0\xa1\xd0\xbe\xd0\xb2\xd0\xb5\xd1\x82\xd0\xbe\xd0\xb2 \xd0\xb4.1 \xd0\xba\xd0\xb2.77","DATARAB":"2012-03-26T00:00:00","DATAUVOLN":null,"NOTES":"","PRIZNUVOLN":0,"PRICHINAUV":"","TELEFON":"914-464-77-28","FOTO":""}]'

        value = json.loads(j.decode("utf-8"), object_hook=Master.decoder)
        return value

    def loadJson(strJson):
        value = []

        try:
            value = json.loads(strJson.decode("utf-8"), object_hook=Master.decoder)
        except Exception as ex:
            print("Ошибка загрузки JSON Master {}".format(ex))

        return value

    def as_json(self):
        d = dict()
        d['IDMASTER'] = self.IDMASTER
        d['SHOTNAMEMASTER'] = self.SHOTNAMEMASTER
        d['FULLNAMEMASTER'] = self.FULLNAMEMASTER
        d['BIRTHDAY'] = self.BIRTHDAY
        d['BIRTHPLACE'] = self.BIRTHPLACE
        d['ADRESSREGISTR'] = self.ADRESSREGISTR
        d['DATARAB'] = self.DATARAB
        d['DATAUVOLN'] = self.DATAUVOLN
        d['NOTES'] = self.NOTES
        d['PRIZNUVOLN'] = self.PRIZNUVOLN
        d['PRICHINAUV'] = self.PRICHINAUV
        d['TELEFON'] = self.TELEFON
        d['FOTO'] = self.FOTO
        d['login'] = self.login
        d['password'] = self.password
        d['HASH'] = self.HASH
        return d

class Static(db.Model):
    __tablename__ = 'Static'
    id = db.Column(db.Integer, primary_key=True)
    idUser = db.Column(db.String(200))
    nameTable = db.Column(db.String(200))
    IdTable = db.Column(db.Integer)
    operator = db.Column(db.String(200))
    success = db.Column(db.String(100))
    dateUpdate = db.Column(db.String(50))
    text = db.Column(db.String)
    error = db.Column(db.String(200))
    write = db.Column(db.String(100))

    def __init__(self, id = None,
                 idUser = None,
                 nameTable = None,
                 IdTable = None,
                 operator = None,
                 success = None,
                 dateUpdate = None,
                 text = None,
                 error = None,
                 write = "False"):
        self.id = id
        self.idUser = idUser
        self.nameTable = nameTable
        self.IdTable = IdTable
        self.operator = operator
        self.success = success
        self.dateUpdate = dateUpdate
        self.text = text
        self.error = error
        self.write = write

    def as_json(self):
        d = dict()
        d['id'] = self.id
        d['idUser'] = self.idUser
        d['nameTable'] = self.nameTable
        d['IdTable'] = self.IdTable
        d['operator'] = self.operator
        d['success'] = self.success
        d['dateUpdate'] = self.dateUpdate
        d['text'] = self.text
        d['error'] = self.error
        d['write'] = self.write
        return d

class Declaration(db.Model):
    __tablename__ = 'Declaration'
    DECLID = db.Column(db.Integer, primary_key=True)
    DECLN = db.Column(db.Integer)
    DECLDATA = db.Column(db.String(100))
    KVN = db.Column(db.Integer)
    TELEFON = db.Column(db.String(100))
    FIO = db.Column(db.String(100))
    DECLARATION = db.Column(db.String(200))
    DECLTIME = db.Column(db.String(100))
    PODCOD = db.Column(db.Integer)
    MASTERID = db.Column(db.Integer)
    DATAVIPOLN = db.Column(db.String(200))
    SOSTZAKAZID = db.Column(db.Integer)
    NOTES = db.Column(db.String(200))
    ZAPLANIR = db.Column(db.String(100))
    USERNAME = db.Column(db.String(100))
    ADRESS = db.Column(db.String(200))

    def __init__(self,
                 DECLID = None,
                 DECLN = None,
                 DECLDATA = None,
                 KVN = None,
                 TELEFON = None,
                 FIO = None,
                 DECLARATION = None,
                 DECLTIME = None,
                 PODCOD = None,
                 MASTERID = 0,
                 DATAVIPOLN = None,
                 SOSTZAKAZID = None,
                 NOTES = None,
                 ZAPLANIR = None,
                 USERNAME = None,
                 ADRESS = None,):
        self.DECLID = DECLID
        self.DECLN = DECLN
        self.DECLDATA = DECLDATA
        self.KVN = KVN
        self.TELEFON = TELEFON
        self.FIO = FIO
        self.DECLARATION = DECLARATION
        self.DECLTIME = DECLTIME
        self.PODCOD = PODCOD
        self.MASTERID = MASTERID
        self.DATAVIPOLN = DATAVIPOLN
        self.SOSTZAKAZID = SOSTZAKAZID
        self.NOTES = NOTES
        self.ZAPLANIR = ZAPLANIR
        self.USERNAME = USERNAME
        self.ADRESS = ADRESS

    def as_json(self):
        d = dict()
        d['DECLID'] = self.DECLID
        d['DECLN'] = self.DECLN
        d['DECLDATA'] = self.DECLDATA
        d['KVN'] = self.KVN
        d['TELEFON'] = self.TELEFON
        d['FIO'] = self.FIO
        d['DECLARATION'] = self.DECLARATION
        d['DECLTIME'] = self.DECLTIME
        d['PODCOD'] = self.PODCOD
        d['MASTERID'] = self.MASTERID
        d['DATAVIPOLN'] = self.DATAVIPOLN
        d['SOSTZAKAZID'] = self.SOSTZAKAZID
        d['NOTES'] = self.NOTES
        d['ZAPLANIR'] = self.ZAPLANIR
        d['USERNAME'] = self.USERNAME
        d['ADRESS'] = self.ADRESS
        return d

    def __repr__(self):
        return "{}".format(self.DECLID)

    def __str__(self):
        return "{}".format(self.DECLID)

    def decoder(obj):
        return Declaration(
            DECLID = obj.get('DECLID'),
            DECLN = obj.get('DECLN'),
            DECLDATA = obj.get('DECLDATA'),
            KVN = obj.get('KVN'),
            TELEFON = obj.get('TELEFON'),
            FIO = obj.get('FIO'),
            DECLARATION = obj.get('DECLARATION'),
            DECLTIME = obj.get('DECLTIME'),
            PODCOD = obj.get('PODCOD'),
            MASTERID = obj.get('MASTERID'),
            DATAVIPOLN = obj.get('DATAVIPOLN'),
            SOSTZAKAZID = obj.get('SOSTZAKAZID'),
            NOTES = obj.get('NOTES'),
            ZAPLANIR = obj.get('ZAPLANIR'),
            USERNAME = obj.get('USERNAME'),
            ADRESS = obj.get('ADRESS'),)

    def loadJson(strJson):
        value = []

        try:
            value = json.loads(strJson.decode("utf-8"), object_hook=Declaration.decoder)
        except Exception as ex:
            print("Ошибка загрузки JSON Declaration {}".format(ex))

        return value