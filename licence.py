from urllib import request
import json
import csv

libs={
      "@angular-devkit/core": "0.0.28",
    "@angular/animations": "5.0.0",
    "@angular/common": "5.0.0",
    "@angular/compiler": "5.0.0",
    "@angular/core": "5.0.0",
    "@angular/forms": "5.0.0",
    "@angular/http": "5.0.0",
    "@angular/platform-browser": "5.0.0",
    "@angular/platform-browser-dynamic": "5.0.0",
    "@angular/router": "5.0.0",
    "@carestack/authentication": "2.1.0",
    "@carestack/configuration": "^0.1.10",
    "@types/applicationinsights-js": "1.0.5",
    "angular2-toaster": "4.0.1",
    "applicationinsights-js": "1.0.14",
    "core-js": "2.4.1",
    "jquery": "3.3.1",
    "moment": "2.20.1",
    "ng2-file-upload": "1.3.0",
    "ng2-select": "2.0.0",
    "ng4-click-outside": "1.0.1",
    "ngx-cookie": "2.0.1",
    "powerbi-client": "2.4.5",
    "rxjs": "5.5.2",
    "zone.js": "0.8.14"
 
  }
c = open('csvfile.csv','w')
c.write('component name,version,url,license,description of how it is used\n') #Give your csv text here.
## Python will convert \n to os.linesep
for lib in libs:
    try:
        with request.urlopen('https://registry.npmjs.org/'+lib) as f:
            str_response = f.read().decode('utf-8')
            package = json.loads(str_response)
            # print(package)
            c.write('\n')
            c.write(lib+',')
            #print(lib)
            c.write(libs[lib]+',')
            c.write(package['repository']['url']+',')
            if 'license' in package:
                c.write("{license}".format(**package)+',')           
            else:
                c.write('no license'+',')
            c.write(package['description']+',')
    except Exception as e:
        print(e)
f.close()