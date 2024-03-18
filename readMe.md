
# How to use Nidd extraction tool(use PM for example)
1.	Go to folder 'DEFINITIONS-extract'
2.	./pm/extract-pms.sh [release number] [username] [password] 
(eg: ./pm/extract-pms.sh 19 dleng 123456789)

## Steps when Nidd extracting
1.	Read all packages in file 'DEFINITIONS-extract\pm\SCRIPT\packages-to-merge',get the packages ids in a release period.

2.	find all the nidds by packageid from website, eg: http://esnidd055.emea.nsn-net.net/NIDD/Trans/Counter?packageId=28319

3. download nidd XML format by URL, eg: http://esnidd055.emea.nsn-net.net/NIDD/Trans/Counter/Export?exportFormat=PiSwMetafileXML&PackageId=XXXXXX

4. execute `saxonb-xslt -ext:on -s:$new_name -xsl:$XSL_DIR/PmDefinitions.xsl -o:$TMP/TEMP/pms.json` convert xml files to json files

5. convert json file to js file.

6. run `diff [newFile] [lastFile]` to find if some changes compare with lastest extration

7. go to result page to check if changes happen. eg: http://hzdleng01.china.nsn-net.net/NIDD-extractions/ALARMS/release-19/2019/04/, if found some cell red, it means changes happened.

    ![avatar](/assets/20190429143308.png)

8. if found changes happen, click the red cell and download the js files, then submit mr.
    ![avatar](/assets/20190429143437.png)



## how to create update mr

1. the nidd defination js files is located at 
    - **alarm**: 
        + `admin\client\components\fault-management\alarm-definitions\i18n\en.js`
    - **faults**:
        + `admin\client\components\fault-management\fault-definitions\i18n\constants\*`
        + `admin\client\components\fault-management\fault-definitions\i18n\en.js`
    - **PM**:
        + `admin\client\components\performance-management\pmDefinitions\i18n\en17.js`
        + `admin\client\components\performance-management\pmDefinitions\i18n\constants\*`
2. download the extracted js files and overwrite them then commit.

3. if you found 19 release need update, you need create mrs to all 19 release branches include unopened branch such as xL19_1_0PD SBTS19A_1_0TD ....

# maintain tool
## run the tool everyday
    ### run `run.sh` and don not close the terminal, it can run extration tool everyday.
## update package id if new package create
1. On menu bar select: PM => Counter List http://esnidd055.emea.nsn-net.net/NIDD/Trans/Counter/Package

2. Select Domain = LTE Product = LTE BTS
Identify from the resulting list the packages you want to extract FL19xxx (Transport) and (Radio)

3. Select Domain = RAN Product = WBTS
Identify from the resulting list the packages you want to extract WBTS19 (Transport) and (Radio)

4. Select Domain = SingleOAM Product = MRBTS PM/FM
Identify from the resulting list the packages you want to extract SBTS19xxx (Transport) and (Radio)

5. For Faults and Alarms use the same method selecting from the top menu: FM => BTS Faults list   and FM => Alarm List

6. if found a new package id, add this id in `packages-to-merge`
     ![avatar](/assets/20190429142615.png)