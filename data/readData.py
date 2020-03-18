import yaml

def read_data(file,key):
    with open('./%s'%file,mode='rb') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)

    return data[key]

def login_data(file,key):
    data = read_data(file,key)
    case_data = data.values()
    data_list = []
    for i in case_data:
        data_list.append(i)

    return data_list






if __name__ == '__main__':
  data = login_data('login.yml','test_login')
  print(data)
