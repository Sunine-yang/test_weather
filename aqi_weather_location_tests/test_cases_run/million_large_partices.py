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
        self.service = service
        self.yaml=ReadYaml.read_yaml(self.service)[self.service]
        self.check=Result_check('Large_Particles_report')
        self.txt=Write_Data_txt

    def large_particles_check(self,num1):

        sql_data = EasyMysql(self.service).query_all(self.yaml['150million_sql'] % (num1))
        self.txt.write_data('/sql_data/%s'%num1,'w+',str(sql_data))
        read_sql=eval(self.txt.read_data('/sql_data/%s'%num1))

        for i in range(len(read_sql)):
            sql_data = "%s,%s |" % (read_sql[i][1], read_sql[i][2])
            try:
                get_url=TestAPI.get_location(self.yaml['guangzhou_150million_url']%read_sql[i][-2]).json()
                resultcode=self.check.comparison_check(get_url["resultcode"],'0','| resultcode:(%s/%s)')
                resultinfo=self.check.comparison_check(get_url["resultinfo"],'OK','| resultinfo:(%s/%s)')
                servertime=self.check.comparison_none_check(get_url["servertime"],'| servertime:(%s)')
                data=self.data_check(get_url['data'])
                city_check = self.city_check(get_url["data"]["city"], read_sql[i], sql_data)
                condition_check = self.condition_check(get_url["data"]["condition"])
                dailys_check = self.dailys_check(get_url["data"]["dailys"], sql_data)
                hourlys_check = self.hourlys_check(get_url["data"]["hourlys"])
                result = resultinfo + resultcode + servertime + data + condition_check + city_check + dailys_check + hourlys_check
                if result == '':
                    print(sql_data+'| 检测通过')
                else:
                    print(sql_data + result)
                    self.check.list_data.append(sql_data + result)
            except Exception as e:
                print(sql_data + '| %s 不存在'%e)
                self.check.list_data.append(sql_data + '| %s 不存在'%e)


            
    def data_check(self,get_url):
        
        for a in range(len(get_url)):
            try:
                data_len=self.check.comparison_check(len(get_url), 6,'| 字节长度:(%s/%s)')
                city=self.check.comparison_none_check(get_url['city'],'| city:(%s)')
                condition=self.check.comparison_none_check(get_url['condition'],'| condition:(%s)')
                dailys=self.check.comparison_none_check(get_url['dailys'],'| dailys:(%s)')
                hourlys=self.check.comparison_none_check(get_url['hourlys'],'| hourlys:(%s)')
                liveInfos=self.check.comparison_is_none_check(get_url["liveInfos"],'| liveInfos:(%s)')
                mobilelink=self.check.comparison_is_none_check(get_url["mobilelink"],'| mobilelink:(%s)')
                result = data_len + city + condition + dailys + hourlys + liveInfos + mobilelink 
                if result == '':
                    return ''
                else:
                    return result
            except Exception as e:
                return '| data:%s 不存在'%e
    # 城市信息检验
    def city_check(self, get_url, read_sql, sql_data):
        try:
            city_len=self.check.comparison_check(len(get_url),9,'| 字节长度:(%s/%s)')
            ca=self.check.comparison_none_check(get_url["ca"],'| ca:(%s)')
            citycode=self.check.comparison_check(get_url["citycode"],read_sql[1],'| citycode:(%s/%s)')
            co=self.check.comparison_none_check(get_url["co"],'| co:(%s)')
            countryCode=self.check.comparison_check(get_url["countryCode"],read_sql[11],'| countryCode:(%s/%s)')
            countryname=self.check.comparison_check(get_url["countryname"],read_sql[3],'| countryname:(%s/%s)')
            name=self.check.comparison_check(get_url["name"],read_sql[2],'| name:(%s/%s)')
            parentcity=self.check.comparison_is_none_check(get_url["parentcity"],'| parentcity:(%s)')
            provincename=self.check.comparison_is_none_check(get_url["provincename"],'| provincename:(%s/%s)')
            timezone=self.check.comparison_check(get_url["timezone"],read_sql[-5],'| timezone:(%s/%s)')
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
                    get_url["updatetime"]) < Data_analysis.hour_time_handle()-2:
                self.check.list_data.append(get_url["updatetime"]) ,Data_analysis.hour_time_handle()
            else:
                condition_len=self.check.comparison_check(len(get_url), 27,'| condition_len:(%s/%s)')
                cloudCover=self.check.comparison_none_check(get_url["cloudCover"],'| cloudCover:(%s)')
                cnweatherid=self.check.comparison_none_check(get_url["cnweatherid"],'| cnweatherid:(%s)')
                comfortlink=self.check.comparison_none_check(get_url["comfortlink"],'| comfortlink:(%s)')
                compareFlag=self.check.comparison_none_check(get_url["compareFlag"],'| compareFlag:(%s)')
                expiretime=self.check.comparison_none_check(get_url["feelTemperatureShade"],'| feelTemperatureShade:(%s)')
                feelTemperatureShade =self.check.comparison_none_check(get_url["humidity"],'| humidity:(%s)')
                humidity=self.check.comparison_none_check(get_url["mobilelink"],'| mobilelink:(%s)')
                mobilelink=self.check.comparison_none_check(get_url["pressure"],'| pressure:(%s)')
                precipitation=self.check.comparison_none_check(get_url["pressureTendency"],'| precipitation:(%s)')
                pressure=self.check.comparison_none_check(get_url["pressure"],'| pressure:(%s)')
                pressureTendency=self.check.comparison_none_check(get_url["pressureTendency"],'| pressureTendency:(%s)')
                realfeel=self.check.comparison_none_check(get_url["realfeel"],'| realfeel:(%s)')
                temperature=self.check.comparison_none_check(get_url["temperature"],'| temperature:(%s)')
                uVIndex=self.check.comparison_none_check(get_url["uVIndex"],'| uVIndex:(%s)')
                updatetime=self.check.comparison_none_check(get_url["updatetime"],'| updatetime:(%s)')
                uvIndexDesc=self.check.comparison_none_check(get_url["uvIndexDesc"],'| uvIndexDesc:(%s)')
                visibility=self.check.comparison_none_check(get_url["visibility"],'| visibility:(%s)')
                weatherid=self.check.comparison_none_check(get_url["weatherid"],'| weatherid:(%s)')
                weathertext=self.check.comparison_none_check(get_url["weathertext"],'| weathertext:(%s)')
                winddegrees=self.check.comparison_none_check(get_url["winddegrees"],'| winddegrees:(%s)')
                winddir=self.check.comparison_none_check(get_url["winddir"],'| winddir:(%s)')
                winddirtext=self.check.comparison_none_check(get_url["winddirtext"],'| winddirtext:(%s)')
                windgustdir=self.check.comparison_none_check(get_url["windgustdir"],'| windgustdir:(%s)')
                windgustlevel=self.check.comparison_none_check(get_url["windgustlevel"],'| windgustlevel:(%s)')
                windgustspeed=self.check.comparison_none_check(get_url["windgustspeed"],'| windgustspeed:(%s)')
                windlevel=self.check.comparison_none_check(get_url["windlevel"],'| windlevel:(%s)')
                windspeed=self.check.comparison_none_check(get_url["windspeed"],'| windspeed:(%s)')
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
        for l in range(len(get_url)):
            self.check.comparison_check(len(get_url), 3, '| dailys_len:(%s/%s)')
            self.check.comparison_none_check(get_url["dailyweathers"], '| dailyweathers:(%s)')
            self.check.comparison_none_check(get_url["mobilelink"], '| mobilelink:(%s)')
            self.check.comparison_none_check(get_url["publictime"], '| publictime:(%s)')
            if Data_analysis.hour_time_handle()>9 and int(Data_analysis.days_time_handle())>1:
                data=self.check.comparison_check(int(Data_analysis.days_time_handle(get_url["dailyweathers"][0]["publictime"])),
                                            int(Data_analysis.days_time_handle())-1, '| 多天预报时间:(预期:%s/实际:%s)')
                if data=='':
                    pass
                else:
                    self.check.list_data.append(sql_data+data)
            elif Data_analysis.hour_time_handle()>9 and int(Data_analysis.days_time_handle())==1:
                data=self.check.comparison_check(int(Data_analysis.days_time_handle(get_url["dailyweathers"][0]["publictime"])),
                    int(Data_analysis.month_days_check()), '| 多天预报时间:(预期:%s/实际:%s)')
                if data == '':
                    pass
                else:
                    self.check.list_data.append(sql_data + data)
            elif Data_analysis.hour_time_handle()<9 and int(Data_analysis.days_time_handle())==1:
                data=self.check.comparison_check(int(Data_analysis.days_time_handle(get_url["dailyweathers"][0]["publictime"]))\
                    ==int(Data_analysis.month_days_check()), '| 多天预报时间:(预期:%s/实际:%s)') or \
                self.check.comparison_check(int(Data_analysis.days_time_handle(get_url["dailyweathers"][0]["publictime"])) \
                    == int(Data_analysis.month_days_check())-1, '| 多天预报时间:(预期:%s/实际:%s)')
                if data == '':
                    pass
                else:
                    self.check.list_data.append(sql_data + data)
            for m in range(len(get_url["dailyweathers"])):
                try:
                    conditionNight=self.dailyweathers_check(get_url["dailyweathers"][m]["conditionNight"],'conditionNight')
                    conditionDay=self.dailyweathers_check(get_url["dailyweathers"][m]["conditionDay"],'conditionDay')
                    dailyweathers_lens=self.check.comparison_check(len(get_url["dailyweathers"]), 16, '| dailyweathers_len:(%s/%s)')
                    dailyweathers_len=self.check.comparison_check(len(get_url["dailyweathers"][m]), 19,'| dailyweathers_s_len:(%s/%s)')
                    currentFestival=self.check.comparison_is_none_check(get_url["dailyweathers"][m]["currentFestival"], '| currentFestival:(%s)')
                    currentRestrict=self.check.comparison_none_check(get_url["dailyweathers"][m]["currentRestrict"], '| currentRestrict:(%s)')
                    currentlink=self.check.comparison_none_check(get_url["dailyweathers"][m]["currentlink"],'| currentlink:(%s)')
                    maxtemp=self.check.comparison_none_check(get_url["dailyweathers"][m]["maxtemp"],'| maxtemp:(%s)')
                    mintemp=self.check.comparison_none_check(get_url["dailyweathers"][m]["mintemp"],'| mintemp:(%s)')
                    mobilelink=self.check.comparison_none_check(get_url["dailyweathers"][m]["mobilelink"],'| mobilelink:(%s)')
                    moonRise=self.check.comparison_none_check(get_url["dailyweathers"][m]["moonRise"],'| moonRise:(%s)')
                    moonSet=self.check.comparison_none_check(get_url["dailyweathers"][m]["moonSet"],'| moonSet:(%s)')
                    moonphase=self.check.comparison_none_check(get_url["dailyweathers"][m]["moonphase"],'| moonphase:(%s)')
                    publictime=self.check.comparison_none_check(get_url["dailyweathers"][m]["publictime"],'| publictime:(%s)')
                    realFeelTempMax=self.check.comparison_none_check(get_url["dailyweathers"][m]["realFeelTempMax"], '| realFeelTempMax:(%s)')
                    realFeelTempMin=self.check.comparison_none_check(get_url["dailyweathers"][m]["realFeelTempMin"], '| realFeelTempMin:(%s)')
                    source=self.check.comparison_none_check(get_url["dailyweathers"][m]["source"],'| source:(%s)')
                    spanDay=self.check.comparison_none_check(get_url["dailyweathers"][m]["spanDays"],'| spanDays:(%s)')
                    sunRise =self.check.comparison_none_check(get_url["dailyweathers"][m]["sunRise"],'| sunRise:(%s)')
                    sunSet=self.check.comparison_none_check(get_url["dailyweathers"][m]["sunSet"],'| sunSet:(%s)')
                    uvIndex=self.check.comparison_none_check(get_url["dailyweathers"][m]["uvIndex"],'| uvIndex:(%s)')
                    result=dailyweathers_len+dailyweathers_lens+currentlink+currentFestival+currentRestrict+maxtemp+mintemp+\
                        moonphase+moonSet+moonRise+mobilelink+publictime+realFeelTempMin+realFeelTempMax+sunSet+sunRise+spanDay+\
                        source+uvIndex+conditionDay+conditionNight
                    if result=='':
                        return ''
                    else:
                        return result
                except Exception as e:
                    return '%s'%e
    def dailyweathers_check(self,get_url,key):
        try:
            conditionDay_lens = self.check.comparison_check(len(get_url), 18, '| 字节长度:(%s/%s)')
            cloudCovers = self.check.comparison_none_check(get_url["cloudCover"], '| cloudCover:(%s)')
            cnweatherids = self.check.comparison_none_check(get_url["cnweatherid"], '| cnweatherid:(%s)')
            ices = self.check.comparison_none_check(get_url["ice"], '| ice:(%s)')
            iceProbs = self.check.comparison_none_check(get_url["iceProb"], '| iceProb:(%s)')
            precProbs = self.check.comparison_none_check(get_url["precProb"], '| precProb:(%s)')
            rains = self.check.comparison_none_check(get_url["rain"], '| rain:(%s)')
            rainProbs = self.check.comparison_none_check(get_url["rainProb"], '| rainProb:(%s)')
            snows = self.check.comparison_none_check(get_url["snow"], '| snow:(%s)')
            snowProbs = self.check.comparison_none_check(get_url["snowProb"], '| snowProb:(%s)')
            thunProbs = self.check.comparison_none_check(get_url["thunProb"], '| thunProb:(%s)')
            totalLiquids = self.check.comparison_none_check(get_url["totalLiquid"], '| totalLiquid:(%s)')
            weatherids = self.check.comparison_none_check(get_url["weatherid"], '| weatherid:(%s)')
            weathertexts = self.check.comparison_none_check(get_url["weathertext"], '| weathertext:(%s)')
            windGustDirs = self.check.comparison_none_check(get_url["windGustDir"], '| windGustDir:(%s)')
            windGustPows = self.check.comparison_none_check(get_url["windGustPow"], '| windGustPow:(%s)')
            winddirs = self.check.comparison_none_check(get_url["winddir"], '| winddir:(%s)')
            windlevels = self.check.comparison_none_check(get_url["windlevel"], '| windlevel:(%s)')
            windspeeds = self.check.comparison_none_check(get_url["windspeed"], '| windspeed:(%s)')
            result=conditionDay_lens+cnweatherids+cloudCovers+ices+iceProbs+precProbs+rainProbs+rains+snows+snowProbs+thunProbs+\
                totalLiquids+windspeeds+winddirs+windlevels+weathertexts+weatherids+windGustDirs+windGustPows
            if result=='':
                return ''
            else:
                return result
        except Exception as e:
            return '| %s:%s 不存在'%(key,e)

    # 小时预报检验
    def hourlys_check(self, get_url):
        datas = self.check.time_check(Data_analysis.hour_time_handle() , Data_analysis.hour_time_handle(get_url['hourlyweathers'][0]["date"])
            , '| hourlys:(%d / %d)')
        for h in range(len(get_url)):
            lens=self.check.comparison_check(len(get_url), 2, '| 字节长度:(%s/%s)')
            expiretime=self.check.comparison_none_check(get_url["expiretime"])
            hourlyweathers=self.hourlyweathers_check(get_url["hourlyweathers"])
            result= lens+expiretime+hourlyweathers+datas
            if result=='':
                return ''
            else:
                return result
    def hourlyweathers_check(self,get_url):
        for u in range(len(get_url)):
            try:
                self.check.comparison_check(len(get_url), 72, '| hourlyweathers_len:(%s/%s)')
                Isdaynight = self.check.comparison_none_check(get_url[u]["Isdaynight"],'| Isdaynight:(%s)')
                cloudCover = self.check.comparison_none_check(get_url[u]["cloudCover"],'| cloudCover:(%s)')
                cnweatherid = self.check.comparison_none_check(get_url[u]["cnweatherid"],'| cnweatherid:(%s)')
                date = self.check.comparison_none_check(get_url[u]["date"],'| date:(%s)')
                dewTemp = self.check.comparison_none_check(get_url[u]["dewTemp"],'| dewTemp:(%s)')
                humidity = self.check.comparison_none_check(get_url[u]["humidity"],'| humidity:(%s)')
                mobilelink = self.check.comparison_none_check(get_url[u]["mobilelink"],'| mobilelink:(%s)')
                rainprobability = self.check.comparison_none_check(get_url[u]["rainprobability"],'| rainprobability:(%s)')
                realfeel = self.check.comparison_none_check(get_url[u]["realfeel"],'| realfeel:(%s)')
                temp = self.check.comparison_none_check(get_url[u]["temp"],'| temp:(%s)')
                uVIndex = self.check.comparison_none_check(get_url[u]["uVIndex"],'| uVIndex:(%s)')
                visibility = self.check.comparison_none_check(get_url[u]["visibility"],'| visibility:(%s)')
                wd = self.check.comparison_none_check(get_url[u]["wd"],'| wd:(%s)')
                wdGust = self.check.comparison_none_check(get_url[u]["wdGust"],'| wdGust:(%s)')
                weatherid = self.check.comparison_none_check(get_url[u]["weatherid"],'| weatherid:(%s)')
                wp = self.check.comparison_none_check(get_url[u]["wp"],'| wp:(%s)')
                wpGust = self.check.comparison_none_check(get_url[u]["wpGust"],'| wpGust:(%s)')
                wsGust = self.check.comparison_none_check(get_url[u]["wsGust"],'| wsGust:(%s)')
                result = Isdaynight + cloudCover + cnweatherid + date + dewTemp + humidity + mobilelink + rainprobability + realfeel\
                         + temp + uVIndex + visibility + wd + wdGust + weatherid + wp + wpGust + wsGust
                if result=='':
                    return ''
                else:
                    data_report='| 小时天气 %s'%Data_analysis.time_transform(get_url[u]["date"])+result
                    return data_report
            except Exception as e:
                return '| 小时天气%s'%e
    def large_particles_start(self,num1,name):
        self.large_particles_check(num1)
        self.check.wait_data_log('300万站点 错误数：%d'%(len(self.check.list_data)))
        self.check.all_wait_data()
        if Data_analysis.document_check('Large_Particles_report')==None:
            pass
        else:

            Test_mail("[vivo]-[%s]-[数据]-[300万站点]-[%d0000]-[%d]"%(name,int(num1)+1,(len(self.check.list_data))), 'Large_Particles_report').smtp_on()
            Data_analysis.data_delete('Large_Particles_report')
        self.check.list_data.clear()
if __name__ == '__main__':
    Large_Particles('guangzhou').large_particles_start(0,'全国')
    # Large_Particles().large_particles_start(10001,20000,'全国')
    # Large_Particles().large_particles_start(20000,30000,'全国')
    # Large_Particles().large_particles_start(30001,40000,'全国')
    # Large_Particles().large_particles_start(40001,50000,'全国')
    # Large_Particles().large_particles_start(50001,60000,'全国')
    # Large_Particles().large_particles_start(60001,70000,'全国')
    # Large_Particles().large_particles_start(70001,80000,'全国')
    # Large_Particles().large_particles_start(80001,90000,'全国')
    # Large_Particles().large_particles_start(90001,100000,'全国')
