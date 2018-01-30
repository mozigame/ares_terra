import requests
import time
from uaa import configureRead
# Authorization = 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1MTY5ODg4MDMsInVzZXJfbmFtZSI6IlBMQVRfeHFfZG91YmxlfHRlc3QyIiwiYXV0aG9yaXRpZXMiOlsiUk9MRV9QTEFURk9STSJdLCJqdGkiOiIwYWY0NWMxYy1mYWQ4LTQ5N2YtODgzMy03YThkMjJiYzcxZGQiLCJjbGllbnRfaWQiOiJ3ZWJfYXBwIiwic2NvcGUiOlsib3BlbmlkIl19.mzm602lXxcuNJ1kqJhnK-t5QDANU0Xjn7nEzVpHGk1zVC8ax94Us03YF3842U5SVSUpn9c_orO0xieb_dIlm9zxfm51i618z0np_Md_0MBY3fzax0yxY7e_8bJ5jVFPG_RIEyvzEj5gBF2enCJNR82-J_DIXtstEraTqN1QpyDnY3CQkQonmCNUXF4rMC9xYVjQEWJKfkaLChE_aWfit-xY2p3ZTGsR-X8luCFsa3LjAfuwPbyJgd_3v2BjRnMrVoCDzGEOagS-LGIhP2M0fsWqj7TBwoj9DE_NQmylhGIdrrKthM4H8oAyvlak4rKygwhL_tfr4SVv3QCpz07Gedg'


agent_authorization = ''


class RequestServer():
    _Authorization=''
    def __init__(self, pc, data):
        self.pc = pc
        self.data = data

    def request(self, self_headers=None, login_model=None):
        headers={}
        if not self_headers:
            headers = {'Authorization': RequestServer._Authorization}
        if self_headers:
            headers = dict(headers, **self_headers)
        #print('login_model='+login_model+' Origin='+self_headers['Origin'])
        #print(headers)
        result={};
        if self.pc.get_method() == 'get':
            result= requests.get(url=self.pc.get_path(), params=self.data, headers=headers)
        elif self.pc.get_method() == 'post':
            result= requests.post(self.pc.get_path(), data=self.data, headers=headers)
        else:
            Exception('未指定请求方法')

        return result;


    #合并功能，支持所有登入类型
    def getToken(loginModel=None):
        loginType = loginModel;
        apiRoot = configureRead.getConfig('api', 'apiRoot');
        print(apiRoot)

        if(apiRoot.find('9999')<0):
            apiRoot=apiRoot+'/uaa';

        if(loginModel=='member'):
            login_path=apiRoot+'/apid/member/login';
        if(loginModel=='agent' or loginModel=='plat'):
            login_path = apiRoot + '/apid/plat/login';
        elif(loginModel=='control'):
            login_path = apiRoot + '/apid/control/login';
        else:
            Exception('Inivalid loginModel:'+loginModel)


        grant_type = 'password'
        account = configureRead.getConfig(loginType, 'account');
        pw = configureRead.getConfig(loginType, 'pw');

        params = ['grant_type', 'username', 'password','code']
        login_data = {params[0]: grant_type, params[1]: account, params[2]: pw, params[3]: '000000_test'}
        if(loginModel=='control'):
            login_header = {'Authorization': 'Basic d2ViX2FwcDo=',
                            'clientId': 'clientId'}
        else:
            origin = configureRead.getConfig(loginType, 'origin')
            login_header = {'Origin': origin, 'Authorization': 'Basic d2ViX2FwcDo=',
                        'clientId': 'clientId'}
        result = requests.post(url=login_path, data=login_data, headers=login_header)
        if (not RequestServer._Authorization and result and result.json()['err'] == 'SUCCESS'):
            RequestServer._Authorization = 'Bearer ' + result.json()['data']['access_token']
            #print(RequestServer._Authorization)
        else:
            print(result.text)
        return result

def datetime_timestamp(dt):
    # dt为字符串
    # 中间过程，一般都需要将字符串转化为时间数组
    time.strptime(dt, '%Y-%m-%d %H:%M:%S')
    ## time.struct_time(tm_year=2012, tm_mon=3, tm_mday=28, tm_hour=6, tm_min=53, tm_sec=40, tm_wday=2, tm_yday=88, tm_isdst=-1)
    # 将"2012-03-28 06:53:40"转化为时间戳
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return int(s)
