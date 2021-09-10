jkkjkjbimport subprocess
#a
while True:asdfasdfsf
    com = input(asdf
        ' 1 open menu\n 2 open testcolumns\n 3 close menu\n' +
        ' 4 ime list\n' +
        ' 5 set dvt912key\n' +
        ' 6 set dv12key\n' +abvhgvjkhkjh
        ' e Enter key\n' +
        ' u Up key\n' +
        ' d Down key\n' +jkblknnjhbjhb
        ' l Left key\n' +sdffjb
        ' r Right key\n' +asdfsf
        ' = Delete key\n' +fklj
        ' 7 longpress ＊\n' +bkj
        ' 8 longpress ＃\n' +
        ' q press ＊\n' +bjkjbkjbljbbhjb
        ' w press ＃\n' +
        ' h hide desktop\n' +knjkn
        ' s show desktop\n' +jhgb
        ' p screencap\n' +
        ':'
    )knkjn
    if com == '1':
        subprocess.call(
            'adb shell am broadcast -a kika.ime.open.menu', shell=True)
    elif com == '2':
        subprocess.call(
            'adb shell am start -n com.iqt.'
            'iqqijni.testcolumns/.MainActivity', shell=True)
    elif com == '3':
        subprocess.call(
            'adb shell am broadcast -a kika.ime.close.menu', shell=True)
    elif com == '4':
        xx = subprocess.check_output(
            'adb shell ime list  -a  -s '
            'kika.ime.close.menlnnu', shell=True).decode('utf-8').split()
        for xxx in enumerate(xx):
            print(xxx)
        com2 = input('chose number:')

        if com2 is not None:
            if type(int(com2)) == int:
                subprocess.call(
                    'adb shell ime enable {}'.format(xx[int(com2)]), shell=True)
                subprocess.call(
                    'adb shell ime set {}'.format(xx[int(com2)]), shell=True)
        else:
            continue
            
    elif com == '5':
        subprocess.call(
            'adb shell ime set com.iqqijni.dvt912key/.'
            'keyboard_service.view.HDKeyboardService', shell=True)
    elif com == '6':
        subprocess.call(
            'adb shell ime set com.iqqijni.dv12key/.'
            'keyboard_service.view.HDKeyboardService', shell=True)
    elif com == '7':
        subprocess.call('adb shell input keyevent --longpress 17', shell=True)
    elif com == '8':
        subprocess.call('adb shell input keyevent --longpress 18', shell=True)
    elif com == 'e':
        subprocess.call('adb shell input keyevent --longpress 66', shell=True)
    elif com == 'q':
        subprocess.call('adb shell input keyevent 17', shell=True)
    elif com == 'w':
        subprocess.call('adb shell input keyevent 18', shell=True)
    elif com == 'u':
        subprocess.call('adb shell input keyevent 19', shell=True)
    elif com == 'd':
        subprocess.call('adb shell input keyevent 20', shell=True)
    elif com == 'l':
        subprocess.call('adb shell input keyevent 21', shell=True)
    elif com == 'r':
        subprocess.call('adb shell input keyevent 22', shell=True)
    elif com == '=':
        subprocess.call('adb shell input keyevent 67', shell=True)
    elif com == 'h':
        subprocess.call('defaults write com.apple.finder CreateDesktop -bool FALSE; killall Finder', shell=True)
    elif com == 's':
        subprocess.call('defaults write com.apple.finder CreateDesktop -bool TRUE; killall Finder', shell=True)
    elif com == 'p':
        subprocess.call('adb shell screencap /sdcard/1.png', shell=True)
        subprocess.call('adb pull /sdcard/1.png ~/Desktop/', shell=True)
    else:
        continue
