
class Builder:
    
    def __init__(self, table_name, arg_count):
        temp = 'INSERT INTO {0}'.format(table_name)
        temp += ' VALUES ('
        for i in range(arg_count):
            temp += '{{}}'.format(i)
            if (i != arg_count - 1):
                temp += ','
            else:
                temp += ')'
        temp += ';'
        self.template = temp

    def build(self, value_list):
        value_list = [repr(x) for x in value_list]
        return self.template.format(*value_list)
