
# def check_json(src_data, dst_data):
#     """
#     校验的json
#     :param src_data:  校验内容
#     :param dst_data:  接口返回的数据（被校验的内容
#     :return:
#     """
#     result = 'success'
#     try:
#         if isinstance(src_data, dict):
#             """若为dict格式"""
#             for key in src_data:
#                 if key not in dst_data:
#                     result = 'fail'
#                 else:
#                     if src_data[key] != dst_data[key]:
#                         result = False
#                     this_key = key
#                     """递归"""
#                     if isinstance(src_data[this_key], dict) and isinstance(dst_data[this_key], dict):
#                         check_json(src_data[this_key], dst_data[this_key])
#                     elif isinstance(type(src_data[this_key]), type(dst_data[this_key])):
#                         result = 'fail'
#                     else:
#                         pass
#             return result
#         return 'fail'
#
#     except Exception as e:
#         return '判断异常'

# print('key和value的交集:', a.items() & b.items())
# print('a中存在的b不存在:', a.items() - b.items())
# print('key和value的并集:', a.items() | b.items())

class Check(object):

    result = 'success'

    def check_json(self,src_data, dst_data):
        """
        校验的json
        :param src_data:  校验内容
        :param dst_data:  接口返回的数据（被校验的内容
        :return:
        """

        try:
            if isinstance(src_data, dict):
                """若为dict格式"""
                for key in src_data:

                    if key not in dst_data:  #不存在则失败
                        self.result = 'fail'
                    else:
                        if isinstance(src_data[key], dict) and isinstance(dst_data[key], dict):

                            self.check_json(src_data[key], dst_data[key])

                        elif src_data[key] != dst_data[key]:
                            print("\033[031m AssertionError",key,src_data[key],"not assert",dst_data[key])
                            self.result = False


                return self.result

            return 'fail'

        except Exception as e:
            return '判断异常'



if __name__ == '__main__':

    new = {
            "code":1,
            "ss":{
                'id':2,
                'name':2
                # 'create_time': 455522222
            }
        }


    old = {
        "code":1,
        "ss":{
            'id':2,
            'name':2,
            'create_time':455522222
        }
    }

    print(Check().check_json(new,old))
