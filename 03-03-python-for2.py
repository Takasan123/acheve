WEEK_LIST = ['月', '火', '水', '木', '金', '土', '日']
SUBJECT_LIST = ['Python', '数学', '機械学習', '深層学習','エンジニアプロジェクト']
#次の日の授業は前日の最後の次の授業から始まることに注意してください。

def output_schedule(study_time_list):
   '''今週の勉強予定を出力します'''
   #科目のインデックス
   subject_index = 1
#２つの配列の要素を２つの変数にアンパック
   for num,week_list_index in zip(study_time_list,range(0,len(WEEK_LIST),1)):

       #勉強時間が0のみを捕まえる
       if num == 0:
           print('{}曜日は、お休みです'.format(WEEK_LIST[week_list_index]))
       #木曜日以外のスケジュールを表示
       #intは文字列と繋げられないのでstrで変換
       else:
           print('{0}曜日は{1}時間勉強する予定です'.format(WEEK_LIST[week_list_index],str(num)))

           #numは曜日ごとに回す回数
           for index in range(num):
               #科目のインデックスが４を超えたら０に戻す
               if subject_index > 4:
                   subject_index = 0
               print('{0}時限目 {1}'.format(index+1,SUBJECT_LIST[subject_index]))
               #回し終わったら+1
               subject_index += 1






def main():
   '''勉強情報をoutput_scheduleに渡します'''
   # 1日に何時間勉強するか（1週間　月曜日〜日曜日）

   study_time_list = [3, 1, 3, 0, 4, 2, 2]
   output_schedule(study_time_list)


if __name__ == '__main__':
   main()