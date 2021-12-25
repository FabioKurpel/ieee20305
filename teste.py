from flask import Flask, request, jsonify, g, request
import sqlite3
#from dicttoxml import dicttoxml
#import xmltodict
import re
import random
path = "http://localhost:5000/"
app = Flask(__name__)

# conn = sqlite3.connect('database.db')
# conn.execute('CREATE TABLE IF NOT EXISTS edevlist (DeviceID TEXT, ConfigurationLink TEXT, DeviceInformationLink TEXT, DeviceStatusLink TEXT, FileStatusLink TEXT, PowerStatusLink TEXT, sFDI TEXT, changedTime TEXT, FunctionSetAssignmentsListLink TEXT, RegistrationLink TEXT, SubscriptionListLink TEXT)')
# conn.execute('delete from edevlist')
# conn.execute("INSERT INTO edevlist VALUES ('1', '/edev/3/cfg', '/edev/3/di', '/edev/3/ds', '/edev/3/fs', '/edev/3/ps', '987654321005', '1379905200', '/edev/3/fsal', '/edev/3/reg', '/edev/3/subl')")
# conn.commit()

def serializer(devList):
    
    xml = """HTTP/1.1 200 OK \nContent-Type: application/sep+xml \nContent-Length: {contentLength} \n\n<EndDeviceList all="1" href="/edev" results=\""""
    
    xml += str(len(devList))
    
    xml += """\" subscribable="0" \nxmlns="urn:ieee:std:2030.5:ns">\n"""
    
    for device in devList:
        device = list(device)
        xml += """\t<EndDevice href="/edev/""" + device[0] + """\" subscribable="0"> \n"""
        xml += """\t\t<ConfigurationLink href=\"""" + device[1] + """\"/> \n"""
        xml += """\t\t<DeviceInformationLink href=\"""" + device[2] + """\"/> \n"""
        xml += """\t\t<DeviceStatusLink href=\"""" + device[3] + """\"/> \n"""
        xml += """\t\t<FileStatusLink href=\"""" + device[4] + """\"/> \n"""
        xml += """\t\t<PowerStatusLink href=\"""" + device[5] + """\"/> \n"""
        xml += "\t\t<sFDI>" + device[6] + "</sFDI> \n"
        xml += "\t\t<changedTime>" + device[7] + "</changedTime> \n"
        xml += """\t\t<FunctionSetAssignmentsListLink all="3" href=\"""" + device[8] + """\"/> \n"""
        xml += """\t\t<RegistrationLink href=\""""  + device[9] + """\"/> \n"""
        xml += """\t\t<SubscriptionListLink all="0" href=\"""" + device[10] + """\"/> \n"""
        xml += "\t</EndDevice> \n"

    
    xml += '</EndDeviceList> \n'
    
    return xml


@app.route('/edev', methods = ['POST', 'GET'])
def raiz():
    if request.method == 'POST':
        data = str(request.data)
    
        sFDI = re.findall("<sFDI>(.*?)</sFDI>", data)[0]
        changedTime = re.findall("<changedTime>(.*?)</changedTime>", data)[0]
    
        print(sFDI)
        print(changedTime)
    
        id = random.randint(1, 100000)
        conn = sqlite3.connect('database.db')
        #conn.cursor().execute("""MAX(deviceid) FROM edevlist""")
        conn.execute("INSERT INTO edevlist VALUES ('2', '/edev/2/cfg', '/edev/2/di', '/edev/2/ds', '/edev/2/fs', '/edev/2/ps', '987654321005', '1379905200', '/edev/2/fsal', '/edev/2/reg', '/edev/2/subl')")
        conn.commit()
    
        return("""HTTP/1.1 201 Created
                Location: /edev/""" + str(id))
                
    if request.method == 'GET':
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT * FROM edevlist""")
        return( serializer(cursor.fetchall())  )


# @app.route('/edev/<lang_code>/')
# def index():
#     value = g.lang_code
#     xml = 'a'
#     return(xml)


# if __name__ == "__main__":
#     """
#     Here you can change debug and port
#     Remember that, in order to make this API functional, you must set debug in False
#     """
#     app.run(ssl_context='adhoc')
    #app.run(host='0.0.0.0', port=5000, debug=False)