import os
import datetime

#現在時刻取得
dateNow = datetime.datetime.now()

#ファイル名定義
fileName = dateNow.strftime('%Y%m%d_%H%M%S%f')[:-3] + '.log' 

#実行ログ記録
logFile = open('.\log\%s' %(fileName), 'w')
logFile.write('[%s]\t%s' %(dateNow.strftime('%Y%m%d_%H:%M:%S.%f')[:-3], 'execute!'))
