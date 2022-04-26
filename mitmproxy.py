from mitmproxy import http
from mitmproxy import ctx
import json
#json.dumps()将Python dict转化为json
#json.loads()将json转化为Python dict
#该用户信息模板为mitmweb抓包结果dict(其中dict特点：①True or "true". ②无Null，需要替换为None.)
temp_info = {
    "data": {
        "groupIds": "168103720247101188,167990053585291761,168109769414935653",
        "selfConfig": {
            "currentInst": {
                "code": "10614",
                "creationTime": None,
                "creator": None,
                "description": "电子科技大学（University of Electronic Science and Technology of China）坐落于四川省会成都市，直属中华人民共和国教育部，由教育部、工业和信息化部、四川省和成都市共建。位列国家“985工程”、“211工程”、“世界一流大学和一流学科”，入选“2011计划”、“111计划”、“卓越工程师教育培养计划”、“国家建设高水平大学公派研究生(硕士)项目”、“中国政府奖学金来华留学生接收院校”，两电一邮成员。是一所完整覆盖整个电子类学科，以电子信息科学技术为核心，以工为主，理工渗透，理、工、管、文、医协调发展的多科性研究型全国重点大学，被誉为“中国电子类院校的排头兵”。",
                "extend": None,
                "id": "93a1e81bc14e4f0e8deae84b68892bb2",
                "lastEditor": "3210343",
                "lastUpdateTime": 1553859803144,
                "name": "电子科技大学"
            },
            "currentOrg": {
                "code": "20",
                "codeLevel": "1",
                "creationTime": 1554816492366,
                "creator": "admin",
                "description": "信息与通信工程学院",
                "enable": True,
                "extend": None,
                "groupTypes": [
                    {
                        "creationTime": 1547886703067,
                        "creator": "admin_lz",
                        "description": "【用户分组】单位（系统内置）",
                        "extend": None,
                        "id": "c5343f6a756d4a3ba124090c89656324",
                        "lastEditor": "3210343",
                        "lastUpdateTime": 1557846213685,
                        "name": "org"
                    }
                ],
                "id": "168109769414935653",
                "institution": None,
                "lastEditor": "admin",
                "lastUpdateTime": 1554816492464,
                "name": "信息与通信工程学院",
                "roleList": None
            },
            "currentReg": {
                "code": "15",
                "codeLevel": "1",
                "creationTime": 1554815050131,
                "creator": "admin",
                "description": "【登记】研究生(硕士)",
                "enable": True,
                "extend": None,
                "groupTypes": [
                    {
                        "creationTime": 1548645587918,
                        "creator": "admin",
                        "description": "【用户分组】登记（系统内置）",
                        "extend": None,
                        "id": "19575e0a41e14ba6a664080d234bc1a6",
                        "lastEditor": "3210343",
                        "lastUpdateTime": 1557846115462,
                        "name": "reg"
                    }
                ],
                "id": "168103720247101188",
                "institution": None,
                "lastEditor": "3210343",
                "lastUpdateTime": 1561709610970,
                "name": "【登记】研究生(硕士)",
                "roleList": None
            }
        },
        "userInfo": {
            "adapterList": [
                {
                    "authServiceUrl": "http://smaco-authslot:5000",
                    "code": "uestc-portal",
                    "creationTime": None,
                    "creator": None,
                    "description": "uestc-portal",
                    "extend": None,
                    "id": "1",
                    "inst": "93a1e81bc14e4f0e8deae84b68892bb2",
                    "lastEditor": None,
                    "lastUpdateTime": None,
                    "name": "uestc-portal",
                    "usrgrpPid": None
                }
            ],
            "authType": "【登记】研究生(硕士)",
            "creationTime": 1596940492269,
            "creator": "stateless action",
            "email": None,
            "extend": "{\"obgrpId\":\"168666108373637107\",\"obgrpName\":\"本科\",\"edtime\":\"20251231\"}",
            "id": "344790630733450769",
            "lastEditor": "stateless action",
            "lastUpdateTime": 1649527510416,
            "loginId": "2018011205010",
            "mobilePhone": "19982012143",
            "name": "杨月",
            "openIds": "",
            "password": "",
            "roleList": [
                {
                    "creationTime": 1568019081390,
                    "creator": "3210343",
                    "description": "",
                    "enable": True,
                    "extend": None,
                    "id": "223485441217662110",
                    "lastEditor": "3210343",
                    "lastUpdateTime": 1568019081486,
                    "name": "【角色】学生类登记用户",
                    "permissions": None,
                    "shiroStr": "stuNormal"
                }
            ],
            "salt": "",
            "state": 1,
            "userGroups": [
                {
                    "code": "15",
                    "codeLevel": "1",
                    "creationTime": 1554815050131,
                    "creator": "admin",
                    "description": "【登记】研究生(硕士)",
                    "enable": True,
                    "extend": None,
                    "groupTypes": [
                        {
                            "creationTime": 1548645587918,
                            "creator": "admin",
                            "description": "【用户分组】登记（系统内置）",
                            "extend": None,
                            "id": "19575e0a41e14ba6a664080d234bc1a6",
                            "lastEditor": "3210343",
                            "lastUpdateTime": 1557846115462,
                            "name": "reg"
                        }
                    ],
                    "id": "168103720247101188",
                    "institution": None,
                    "lastEditor": "3210343",
                    "lastUpdateTime": 1561709610970,
                    "name": "【登记】研究生(硕士)",
                    "roleList": None
                },
                {
                    "code": "2",
                    "codeLevel": "1",
                    "creationTime": 1554787949886,
                    "creator": "admin",
                    "description": "【违章】学生用户",
                    "enable": True,
                    "extend": None,
                    "groupTypes": [
                        {
                            "creationTime": 1547886718577,
                            "creator": "admin_lz",
                            "description": "【用户分组】违章（系统内置）",
                            "extend": None,
                            "id": "c1774adae90340b5b32755eb0477f1ff",
                            "lastEditor": "3210343",
                            "lastUpdateTime": 1557846093107,
                            "name": "vio"
                        }
                    ],
                    "id": "167990053585291761",
                    "institution": None,
                    "lastEditor": "3210343",
                    "lastUpdateTime": 1561709665736,
                    "name": "【违章】学生用户",
                    "roleList": None
                },
                {
                    "code": "20",
                    "codeLevel": "1",
                    "creationTime": 1554816492366,
                    "creator": "admin",
                    "description": "信息与通信工程学院",
                    "enable": True,
                    "extend": None,
                    "groupTypes": [
                        {
                            "creationTime": 1547886703067,
                            "creator": "admin_lz",
                            "description": "【用户分组】单位（系统内置）",
                            "extend": None,
                            "id": "c5343f6a756d4a3ba124090c89656324",
                            "lastEditor": "3210343",
                            "lastUpdateTime": 1557846213685,
                            "name": "org"
                        }
                    ],
                    "id": "168109769414935653",
                    "institution": None,
                    "lastEditor": "admin",
                    "lastUpdateTime": 1554816492464,
                    "name": "信息与通信工程学院",
                    "roleList": None
                }
            ]
        }
    },
    "expire": 0,
    "msg": "200 OK",
    "status": 1
}
#出入校授权信息，初始化为入校
temp_pass = '研究生用户，入校授权有效！'
#出校二维码control_id：西大门出校20,西二门出校00,南大门出校11,沙河出校083
out_school = ['1000020$7$0$0',
              '1000000$7$0$0',
              '1000011$7$0$0',
              '083']
#mitmproxy中代理所有HTTP请求的response全部会经过这里
def response(flow: http.HTTPFlow) -> None:
    #—>None：标注函数返回类型为空
    if flow.request.url.startswith("https://smaco2.uestc.edu.cn/shiroApi"):
        data1 = json.loads(flow.response.get_text())
           #若用户已绑定，将模板中名字替换为用户名字
        if data1["status"] == 1:
            temp_info["data"]["userInfo"]["name"] = data1["data"]["userInfo"]["name"]
        flow.response.set_text(json.dumps(temp_info))
        #模板名字复位
        temp_info["data"]["userInfo"]["name"] = '杨月'
    if flow.request.url.startswith("https://smaco2.uestc.edu.cn/passObjectApi/temp/sign?"):
        #扫描结果为出校二维码情况，使用列表简化代码
        if flow.request.url[65:] in out_school:
            #修改全局变量，需要声明
            global temp_pass
            temp_pass = '研究生用户，出校授权有效！'
        data2 = json.loads(flow.response.get_text())
        data2["status"] = 1
        data2["msg"] = temp_pass
        #出入校授权信息，复位为入校
        temp_pass = '研究生用户，入校授权有效！'
        flow.response.set_text(json.dumps(data2))