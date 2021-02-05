#-*-coding:GBK -*-
import time

from lib.test_api import TestAPI
from tools.easy_mysql import EasyMysql
from tools.read_yaml import ReadYaml
from analysis.comparison_results import Result_check
from analysis.data_analysis import Data_analysis
from tools.test_html import Test_mail
from tools.write_data_txt import Write_Data_txt

class Large_Particles:
    def __init__(self,service):
        self.yaml=ReadYaml.read_yaml()['large_particles']
        self.check=Result_check('Large_Particles_report')
        self.txt=Write_Data_txt
        self.service=service
    def large_particles_check(self,unm1,num2):


        global result, e
        sql_data = EasyMysql.query_all(self.yaml['150million_sql'] % (unm1, num2))
        self.txt.write_data('/sql_data/%s'%num2,'w+',str(sql_data))
        read_sql=eval(self.txt.read_data('/sql_data/%s'%num2))

        for i in range(len(read_sql)):
            sql_data="%s,%s |"%(read_sql[i][1],read_sql[i][2])
            get_url=TestAPI.get_location(self.yaml[self.service]%read_sql[i][-2]).json()
            self.check.comparison_check(len(get_url),4,'| 字节长度:(%s/%s)')
            self.check.comparison_check(get_url["resultcode"],'0','| resultcode:(%s/%s)')
            self.check.comparison_check(get_url["resultinfo"],'OK','| resultinfo:(%s/%s)')
            self.check.comparison_none_check(get_url["servertime"],'| servertime:(%s)')
            for a in range(len(get_url["data"])):
                try:
                    data_len=self.check.comparison_check(len(get_url["data"]), 6,'| 字节长度:(%s/%s)')
                    city=self.check.comparison_none_check(get_url["data"]["city"],'| city:(%s)')
                    condition=self.check.comparison_none_check(get_url["data"]["condition"],'| condition:(%s)')
                    dailys=self.check.comparison_none_check(get_url["data"]["dailys"],'| dailys:(%s)')
                    hourlys=self.check.comparison_none_check(get_url["data"]["hourlys"],'| hourlys:(%s)')
                    liveInfos=self.check.comparison_is_none_check(get_url["data"]["liveInfos"],'| liveInfos:(%s)')
                    mobilelink=self.check.comparison_is_none_check(get_url["data"]["mobilelink"],'| mobilelink:(%s)')
                    city_check=self.city_check(get_url,read_sql[i],sql_data)
                    condition_check=self.condition_check(get_url)
                    dailys_check=self.dailys_check(get_url,sql_data)
                    hourlys_check=self.hourlys_check(get_url,sql_data)
                    result = data_len + city + condition + dailys + hourlys + liveInfos + mobilelink + city_check + condition_check + dailys_check + hourlys_check
                    if result == '':
                        print(sql_data + '| 检测通过')
                    else:
                        self.check.list_data.append(sql_data + result)
                except Exception as e:
                    self.check.list_data.append(sql_data + '| %s 不存在'%e)





    # 城市信息检验
    def city_check(self, get_url, read_sql, sql_data):
        try:
            city_len=self.check.comparison_check(len(get_url["data"]["city"]),9,'| 字节长度:(%s/%s)')
            ca=self.check.comparison_none_check(get_url["data"]["city"]["ca"],'| ca:(%s)')
            citycode=self.check.comparison_check(get_url["data"]["city"]["citycode"],read_sql[1],'| citycode:(%s/%s)')
            co=self.check.comparison_none_check(get_url["data"]["city"]["co"],'| co:(%s)')
            countryCode=self.check.comparison_check(get_url["data"]["city"]["countryCode"],read_sql[11],'| countryCode:(%s/%s)')
            countryname=self.check.comparison_check(get_url["data"]["city"]["countryname"],read_sql[3],'| countryname:(%s/%s)')
            name=self.check.comparison_check(get_url["data"]["city"]["name"],read_sql[2],'| name:(%s/%s)')
            parentcity=self.check.comparison_is_none_check(get_url["data"]["city"]["parentcity"],'| parentcity:(%s)')
            provincename=self.check.comparison_is_none_check(get_url["data"]["city"]["provincename"],'| provincename:(%s/%s)')
            timezone=self.check.comparison_check(get_url["data"]["city"]["timezone"],read_sql[-5],'| timezone:(%s/%s)')
            result=city_len+ca+citycode+co+countryCode+countryname+countryname+name+parentcity+provincename+timezone
            if result=='':
                return ''
            else:
                return result
        except Exception as e:
            return '| city:%s 不存在'%e
    def condition_check(self,get_url):

        try:
            if Data_analysis.hour_time_handle(
                    get_url["data"]["condition"]["updatetime"]) < Data_analysis.hour_time_handle()-2:
                self.check.list_data.append(get_url["data"]["condition"]["updatetime"]) ,Data_analysis.hour_time_handle()
            else:
                condition_len=self.check.comparison_check(len(get_url["data"]["condition"]), 27,'| condition_len:(%s/%s)')
                cloudCover=self.check.comparison_none_check(get_url["data"]["condition"]["cloudCover"],'| cloudCover:(%s)')
                cnweatherid=self.check.comparison_none_check(get_url["data"]["condition"]["cnweatherid"],'| cnweatherid:(%s)')
                comfortlink=self.check.comparison_none_check(get_url["data"]["condition"]["comfortlink"],'| comfortlink:(%s)')
                compareFlag=self.check.comparison_none_check(get_url["data"]["condition"]["compareFlag"],'| compareFlag:(%s)')
                expiretime=self.check.comparison_none_check(get_url["data"]["condition"]["feelTemperatureShade"],'| feelTemperatureShade:(%s)')
                feelTemperatureShade =self.check.comparison_none_check(get_url["data"]["condition"]["humidity"],'| humidity:(%s)')
                humidity=self.check.comparison_none_check(get_url["data"]["condition"]["mobilelink"],'| mobilelink:(%s)')
                mobilelink=self.check.comparison_none_check(get_url["data"]["condition"]["pressure"],'| pressure:(%s)')
                precipitation=self.check.comparison_none_check(get_url["data"]["condition"]["pressureTendency"],'| precipitation:(%s)')
                pressure=self.check.comparison_none_check(get_url["data"]["condition"]["pressure"],'| pressure:(%s)')
                pressureTendency=self.check.comparison_none_check(get_url["data"]["condition"]["pressureTendency"],'| pressureTendency:(%s)')
                realfeel=self.check.comparison_none_check(get_url["data"]["condition"]["realfeel"],'| realfeel:(%s)')
                temperature=self.check.comparison_none_check(get_url["data"]["condition"]["temperature"],'| temperature:(%s)')
                uVIndex=self.check.comparison_none_check(get_url["data"]["condition"]["uVIndex"],'| uVIndex:(%s)')
                updatetime=self.check.comparison_none_check(get_url["data"]["condition"]["updatetime"],'| updatetime:(%s)')
                uvIndexDesc=self.check.comparison_none_check(get_url["data"]["condition"]["uvIndexDesc"],'| uvIndexDesc:(%s)')
                visibility=self.check.comparison_none_check(get_url["data"]["condition"]["visibility"],'| visibility:(%s)')
                weatherid=self.check.comparison_none_check(get_url["data"]["condition"]["weatherid"],'| weatherid:(%s)')
                weathertext=self.check.comparison_none_check(get_url["data"]["condition"]["weathertext"],'| weathertext:(%s)')
                winddegrees=self.check.comparison_none_check(get_url["data"]["condition"]["winddegrees"],'| winddegrees:(%s)')
                winddir=self.check.comparison_none_check(get_url["data"]["condition"]["winddir"],'| winddir:(%s)')
                winddirtext=self.check.comparison_none_check(get_url["data"]["condition"]["winddirtext"],'| winddirtext:(%s)')
                windgustdir=self.check.comparison_none_check(get_url["data"]["condition"]["windgustdir"],'| windgustdir:(%s)')
                windgustlevel=self.check.comparison_none_check(get_url["data"]["condition"]["windgustlevel"],'| windgustlevel:(%s)')
                windgustspeed=self.check.comparison_none_check(get_url["data"]["condition"]["windgustspeed"],'| windgustspeed:(%s)')
                windlevel=self.check.comparison_none_check(get_url["data"]["condition"]["windlevel"],'| windlevel:(%s)')
                windspeed=self.check.comparison_none_check(get_url["data"]["condition"]["windspeed"],'| windspeed:(%s)')
                result=windspeed+windlevel+windgustspeed+windgustlevel+windgustdir+winddirtext+winddir+weathertext\
                +weatherid+visibility+uvIndexDesc+updatetime+uVIndex+temperature+realfeel+precipitation+mobilelink\
                       +humidity+feelTemperatureShade+expiretime+compareFlag+comfortlink+cnweatherid+cloudCover+condition_len+pressure+winddegrees+pressureTendency
                if result == '':
                    return ''
                else:
                    return result
        except Exception as e:


            return '| condition:%s 不存在'%e

    # 多天预报检验
    def dailys_check(self, get_url,sql_data):
        global result, dailyweathers_lens, m
        for l in range(len(get_url["data"]["dailys"])):
            self.check.comparison_check(len(get_url["data"]["dailys"]), 3, '| dailys_len:(%s/%s)')
            self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"], '| dailyweathers:(%s)')
            self.check.comparison_none_check(get_url["data"]["dailys"]["mobilelink"], '| mobilelink:(%s)')
            self.check.comparison_none_check(get_url["data"]["dailys"]["publictime"], '| publictime:(%s)')
            if Data_analysis.hour_time_handle()>9 and int(Data_analysis.days_time_handle())>1:
                data=self.check.comparison_check(int(Data_analysis.days_time_handle(get_url["data"]["dailys"]["dailyweathers"][0]["publictime"])),
                                            int(Data_analysis.days_time_handle())-1, '| 多天预报时间:(预期：%s/实际：%s)')
                if data=='':
                    pass
                else:
                    self.check.list_data.append(sql_data+data)
            elif Data_analysis.hour_time_handle()>9 and int(Data_analysis.days_time_handle())==1:
                data=self.check.comparison_check(int(Data_analysis.days_time_handle(get_url["data"]["dailys"]["dailyweathers"][0]["publictime"])),
                    int(Data_analysis.month_days_check()), '| 多天预报时间:(预期：%s/实际：%s)')
                if data == '':
                    pass
                else:
                    self.check.list_data.append(sql_data + data)
            elif Data_analysis.hour_time_handle()<9 and int(Data_analysis.days_time_handle())==1:
                data=self.check.comparison_check(int(Data_analysis.days_time_handle(get_url["data"]["dailys"]["dailyweathers"][0]["publictime"]))\
                    ==int(Data_analysis.month_days_check()), '| 多天预报时间:(预期：%s/实际：%s)') or \
                self.check.comparison_check(int(Data_analysis.days_time_handle(get_url["data"]["dailys"]["dailyweathers"][0]["publictime"])) \
                    == int(Data_analysis.month_days_check())-1, '| 多天预报时间:(预期：%s/实际：%s)')
                if data == '':
                    pass
                else:
                    self.check.list_data.append(sql_data + data)

            for m in range(len(get_url["data"]["dailys"]["dailyweathers"])):
                dailyweathers_lens=self.check.comparison_check(len(get_url["data"]["dailys"]["dailyweathers"]), 16, '| dailyweathers_len:(%s/%s)')
                for o in range(len(get_url["data"]["dailys"]["dailyweathers"][m])):
                    dailyweathers_len=self.check.comparison_check(len(get_url["data"]["dailys"]["dailyweathers"][m]), 19,'| dailyweathers_s_len:(%s/%s)')
                    conditionDay=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"],'| conditionDay:(%s)')
                    conditionNight=self.check.comparison_is_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"], '| conditionNight:(%s)')
                    currentFestival=self.check.comparison_is_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["currentFestival"], '| currentFestival:(%s)')
                    currentRestrict=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["currentRestrict"], '| currentRestrict:(%s)')
                    currentlink=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["currentlink"],'| currentlink:(%s)')
                    maxtemp=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["maxtemp"],'| maxtemp:(%s)')
                    mintemp=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["mintemp"],'| mintemp:(%s)')
                    mobilelink=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["mobilelink"],'| mobilelink:(%s)')
                    moonRise=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["moonRise"],'| moonRise:(%s)')
                    moonSet=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["moonSet"],'| moonSet:(%s)')
                    moonphase=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["moonphase"],'| moonphase:(%s)')
                    publictime=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["publictime"],'| publictime:(%s)')
                    realFeelTempMax=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["realFeelTempMax"], '| realFeelTempMax:(%s)')
                    realFeelTempMin=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["realFeelTempMin"], '| realFeelTempMin:(%s)')
                    source=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["source"],'| source:(%s)')
                    spanDay=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["spanDays"],'| spanDays:(%s)')
                    sunRise =self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["sunRise"],'| sunRise:(%s)')
                    sunSet=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["sunSet"],'| sunSet:(%s)')
                    uvIndex=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["uvIndex"],'| uvIndex:(%s)')
                    conditionDay_lens=self.check.comparison_check(len(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]),18, '| 字节长度:(%s/%s)')
                    cloudCovers=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["cloudCover"],'| cloudCover:(%s)')
                    cnweatherids=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["cnweatherid"], '| cnweatherid:(%s)')
                    ices =self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["ice"], '| ice:(%s)')
                    iceProbs=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["iceProb"], '| iceProb:(%s)')
                    precProbs=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["precProb"],'| precProb:(%s)')
                    rains=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["rain"], '| rain:(%s)')
                    rainProbs=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["rainProb"],'| rainProb:(%s)')
                    snows=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["snow"], '| snow:(%s)')
                    snowProbs =self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["snowProb"],'| snowProb:(%s)')
                    thunProbs=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["thunProb"],'| thunProb:(%s)')
                    totalLiquids=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["totalLiquid"],'| totalLiquid:(%s)')
                    weatherids=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["weatherid"],'| weatherid:(%s)')
                    weathertexts=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["weathertext"],'| weathertext:(%s)')
                    windGustDirs=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["windGustDir"],'| windGustDir:(%s)')
                    windGustPows =self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["windGustPow"],'| windGustPow:(%s)')
                    winddirs=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["winddir"], '| winddir:(%s)')
                    windlevels=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["windlevel"],'| windlevel:(%s)')
                    windspeeds=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionDay"]["windspeed"],'| windspeed:(%s)')
                    # cloudCover_len=self.check.comparison_check(len(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]), 18, '| 字节长度:(%s/%s)')
                    cloudCover=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["cloudCover"],'| cloudCover:(%s)')
                    cnweatherid=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["cnweatherid"],'| cnweatherid:(%s)')
                    ice=self.check.comparison_none_check( get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["ice"], '| ice:(%s)')
                    iceProb=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["iceProb"],'| iceProb:(%s)')
                    precProb=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["precProb"],'| precProb:(%s)')
                    rain=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["rain"], '| rain:(%s)')
                    rainProb=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["rainProb"],'| rainProb:(%s)')
                    snow=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["snow"], '| snow:(%s)')
                    snowProb=self.check.comparison_none_check( get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["snowProb"],'| snowProb:(%s)')
                    thunProb=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["thunProb"],'| thunProb:(%s)')
                    totalLiquid=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["totalLiquid"],'| totalLiquid:(%s)')
                    weatherid=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["weatherid"],'| weatherid:(%s)')
                    weathertext=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["weathertext"],'| weathertext:(%s)')
                    windGustDir=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["windGustDir"],'| windGustDir:(%s)')
                    windGustPow=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["windGustPow"],'| windGustPow:(%s)')
                    winddir=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["winddir"],'| winddir:(%s)')
                    windlevel=self.check.comparison_none_check( get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["windlevel"],'| windlevel:(%s)')
                    windspeed=self.check.comparison_none_check(get_url["data"]["dailys"]["dailyweathers"][m]["conditionNight"]["windspeed"],'| windspeed:(%s)')
                    result=windspeed+windlevel+winddir+windGustPow+windGustDir+weathertext+weatherid+totalLiquid+thunProb+snowProb+snow+\
                           rainProb+rain+precProb+iceProb+ice+cnweatherid+cloudCover+windspeeds+windlevels+winddirs+\
                           windGustPows+windGustDirs+weathertexts+weatherids+totalLiquids+thunProbs+snowProbs+snows+\
                           rainProbs+rains+precProbs+iceProbs+ices+cnweatherids+cloudCovers+conditionDay_lens+uvIndex\
                           +sunSet+sunRise+spanDay+source+realFeelTempMin+realFeelTempMax+publictime+moonphase+moonSet+moonRise+mobilelink+\
                    maxtemp+mintemp+currentlink+currentlink+currentRestrict+currentFestival+conditionNight+conditionDay+dailyweathers_len
            if dailyweathers_lens+result=='':
                return ''
            else:
                report= '| 多天预报 %s'%Data_analysis.time_transform(get_url["data"]["dailys"]["dailyweathers"][m]["publictime"])+dailyweathers_lens+result
                return report

    # 小时预报检验
    def hourlys_check(self, get_url,sql_data):
        datas = self.check.time_check(
            (int(Data_analysis.hour_time_handle(get_url["data"]["hourlys"]["hourlyweathers"][0]["date"])))
            , Data_analysis.hour_time_handle() , '| time:(%s/%s)')
        for h in range(len(get_url["data"]["hourlys"])):
            self.check.comparison_check(len(get_url["data"]["hourlys"]), 2, '| 字节长度:(%s/%s)')
            self.check.comparison_none_check(get_url["data"]["hourlys"]["expiretime"])
            self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"])

            for u in range(len(get_url["data"]["hourlys"]["hourlyweathers"])):
                self.check.comparison_check(len(get_url["data"]["hourlys"]["hourlyweathers"]), 72, '| hourlyweathers_len:(%s/%s)')
                Isdaynight = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["Isdaynight"],'| Isdaynight:(%s)')
                cloudCover = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["cloudCover"],'| cloudCover:(%s)')
                cnweatherid = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["cnweatherid"],'| cnweatherid:(%s)')
                date = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["date"],'| date:(%s)')
                dewTemp = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["dewTemp"],'| dewTemp:(%s)')
                humidity = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["humidity"],'| humidity:(%s)')
                mobilelink = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["mobilelink"],'| mobilelink:(%s)')
                rainprobability = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["rainprobability"],'| rainprobability:(%s)')
                realfeel = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["realfeel"],'| realfeel:(%s)')
                temp = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["temp"],'| temp:(%s)')
                uVIndex = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["uVIndex"],'| uVIndex:(%s)')
                visibility = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["visibility"],'| visibility:(%s)')
                wd = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["wd"],'| wd:(%s)')
                wdGust = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["wdGust"],'| wdGust:(%s)')
                weatherid = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["weatherid"],'| weatherid:(%s)')
                wp = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["wp"],'| wp:(%s)')
                wpGust = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["wpGust"],'| wpGust:(%s)')
                wsGust = self.check.comparison_none_check(get_url["data"]["hourlys"]["hourlyweathers"][u]["wsGust"],'| wsGust:(%s)')
                result = Isdaynight + cloudCover + cnweatherid + date + dewTemp + humidity + mobilelink + rainprobability + realfeel\
                         + temp + uVIndex + visibility + wd + wdGust + weatherid + wp + wpGust + wsGust+datas
                if result=='':
                    return ''
                else:
                    data_report='| 小时天气 %s'%Data_analysis.time_transform(get_url["data"]["hourlys"]["hourlyweathers"][u]["date"])+\
                        result
                    return data_report
    def large_particles_start(self,num1,num2,name):
        self.large_particles_check(num1,num2)
        self.check.wait_data_log('10万站点 错误数：%d'%(len(self.check.list_data)))
        self.check.all_wait_data()
        if Data_analysis.document_check('Large_Particles_report')==None:
            pass
        else:

            Test_mail("[vivo]-[%s]-[数据]-[10万站点]-[%d]"%(name,(len(self.check.list_data))), 'Large_Particles_report').smtp_on()
            Data_analysis.data_delete('Large_Particles_report')
        self.check.list_data.clear()
if __name__ == '__main__':
    Large_Particles('guangzhou_150million_url').large_particles_start(0,100,'全国')
    # Large_Particles().large_particles_start(10001,20000,'全国')
    # Large_Particles().large_particles_start(20000,30000,'全国')
    # Large_Particles().large_particles_start(30001,40000,'全国')
    # Large_Particles().large_particles_start(40001,50000,'全国')
    # Large_Particles().large_particles_start(50001,60000,'全国')
    # Large_Particles().large_particles_start(60001,70000,'全国')
    # Large_Particles().large_particles_start(70001,80000,'全国')
    # Large_Particles().large_particles_start(80001,90000,'全国')
    # Large_Particles().large_particles_start(90001,100000,'全国')
