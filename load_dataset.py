from pandas import DataFrame
import csv

def encode_class(c):
    return c!='normal'

atts = [('duration',float),
        ('protocol_type',str),
        ('service',str),
        ('flag',str),
        ('src_bytes',float),
        ('dst_bytes',float),
        ('land',bool),
        ('wrong_fragment',float),
        ('urgent',float),
        ('hot',float),
        ('num_failed_logins',float),
        ('logged_in',bool),
        ('num_compromised',float),
        ('root_shell',float),
        ('su_attempted',float),
        ('num_root',float),
        ('num_file_creations',float),
        ('num_shells',float),
        ('num_access_files',float),
        ('num_outbound_cmds',float),
        ('is_host_login',bool),
        ('is_guest_login',bool),
        ('count',float),
        ('srv_count',float),
        ('serror_rate',float),
        ('srv_serror_rate',float),
        ('rerror_rate',float),
        ('srv_rerror_rate',float),
        ('same_srv_rate',float),
        ('diff_srv_rate',float),
        ('srv_diff_host_rate',float),
        ('dst_host_count',float),
        ('dst_host_srv_count',float),
        ('dst_host_same_srv_rate',float),
        ('dst_host_diff_srv_rate',float),
        ('dst_host_same_src_port_rate',float),
        ('dst_host_srv_diff_host_rate',float),
        ('dst_host_serror_rate',float),
        ('dst_host_srv_serror_rate',float),
        ('dst_host_rerror_rate',float),
        ('dst_host_srv_rerror_rate',float),
        ('class',encode_class),
        ('difficulty_level',float)]

def load_dataset(filename):
    n=len(atts)
    csvf=open(filename)
    data = [[atts[i][1](r[i]) for i in range(n)] for r in csv.reader(csvf)]
    return DataFrame(data,columns=[a[0] for a in atts])

train_df = load_dataset('KDDTrain+.txt')
test_df = load_dataset('KDDTest+.txt')
print(train_df.dtypes)
