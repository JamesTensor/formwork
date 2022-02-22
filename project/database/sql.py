# coding=utf-8
template = {
'select_record_sql_by_type':'''
select * from formwork where formwork = "{formwork}";
''',
'update_record_sql':'''
UPDATE formwork SET formwork="{formwork}" WHERE formwork="{formwork}";
''',
'insert_formwork_sql':'''
INSERT INTO record(formwork,formwork) values('{formwork}','{formwork}')  ON DUPLICATE KEY UPDATE formwork='{formwork}';
''',
'select_formwork_sql':'''
select * from formwork limit {num1},{num2};
''',
'count_formwork_sql':'''
select count(*) from formwork;
'''
}

python_template = {
'formwork_select_sql':'''
select * from formwork_table
''',
'formwork_sql':'''
p_c.db.ExecNonQuery(s.t["formwork_sql"].format(formwork=p_c.db.secure(g_p_d['formwork'])))
'''
}

t = template