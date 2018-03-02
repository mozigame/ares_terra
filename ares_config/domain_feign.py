import ares_config.config as plat_config
from utils.request_util import *

path = {
    'plat_domains': ['/apis/plat/domains', ('platId',), 'get', '获取平台商域名列表', 'DomainFeignController'],
}


# 获取平台商域名列表
def plat_domains(platId=None):
    pc = PathConfig(path_name='plat_domains', path=path, Config=plat_config.Config)
    data = {'platId': platId}
    return RequestServer(pc, data).request()


if __name__ == '__main__':
    get_token('plat')
    plat_config.Config.env = 'prod'
    # plat_ids = [60, 59, 38, 35, 68, 39, 61, 66, 71, 70, 69, 67, 65, 44, 48, 49, 58, 47, 40, 46, 43, 42, 41, 2, 10, 37,
    #             1]
    plat_ids = [54, 46, 48, 52, 50, 41, 45, 44, 35, 37, 42, 43, 40, 2, 38, 39, 10, 1]
    print_strs=''
    for plat_id in plat_ids:
        result = plat_domains(plat_id)
        result = result.json()
        if result['data'].__len__() > 0:
            print("platId\tagentId\tdomain\ttype\t")
            for plat_domain in result['data']:
                # print(plat_id, result['data'])
                if plat_domain['status'] == 1:
                    print_str= '{}\t{}\t{}\t{}\t{}\n'.format(plat_domain['platId'], plat_domain['agentId'], plat_domain['domain'], plat_domain['type'],
                          plat_domain['status'])
                    print(plat_domain['platId'], plat_domain['agentId'], plat_domain['domain'], plat_domain['type'],
                          plat_domain['status'],
                          sep='\t')
                    print_strs+=print_str
    print("\n\n")
    print(print_strs)