import logs_pb2 as lpb2

# Hacked version of go implementation at
# https://github.com/lyft/protoc-gen-validate

def validate_StringRules(string_rule_type, string_rule_dat, instance):
    if string_rule_type == "in":
        if instance not in string_rule_dat:
            print("ERRROR")
        else:
            print("VALIDATE_SUCCESS")

def getRuleType(field_rules):
    return field_rules.ListFields()[0][0].message_type.name

'''
validate_fns = []

for field in lpb2.VideoEnd.DESCRIPTOR.fields:
    field_options = field.GetOptions()
    for f,v in field_options.ListFields():
        print(field.name, getRuleType(v))
        #print (f.name)
        #print(f)
        #print(v)
'''

ve = lpb2.VideoEnd(log_id=lpb2.VIDEO_END, ev_name="foo", s_pl_cookie="123", u_segment_id=1, u_played_dur=10000, tmp_cookie = {"cookie": "xyz"})

print(ve)

def validate(m):
    for field, val in m.ListFields():
        print("_________", (field.type), field.TYPE_MESSAGE)
        if field.type == field.TYPE_MESSAGE:
            validate(val)
        field_options = field.GetOptions()
        for f,v in field_options.ListFields():
            rule_type = getRuleType(v)
            print(field.name, rule_type, val)
            if rule_type == "StringRules":
                sr_f, sr_v = v.ListFields()[0][1].ListFields()[0]
                print(sr_f.name, sr_v)
                validate_StringRules(sr_f.name, sr_v, val)

validate(ve)
