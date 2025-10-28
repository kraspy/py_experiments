select pg_typeof('{"a": 1}'::json -> 'a');   -- JSON/JSONB-значение

select pg_typeof('{"a": 1}'::json ->> 'a');  -- text

select '[1, 2]'::json -> 1;

select '{"a": 1}'::jsonb ? 'a';

select '{"a": 1}'::jsonb ?| array['a', 'b'];

select '{"a": 1}'::jsonb ?& array['a', 'b'];

select '{"a": 1, "b": 2}'::jsonb @> '{"a": 1}';

select jsonb_object_keys('{"a": 1, "b": 2}'::jsonb);

select jsonb_each('{"a": 1, "b": 2}'::jsonb);

select jsonb_array_elements('[1, 2]'::jsonb);

select jsonb_set('{"a": 1, "b": 2}'::jsonb, '{a}', '3');

select jsonb_array_length('[1,2,3]'::jsonb);

select jsonb_pretty('{"a": 1, "b": 2}');

select *
from
	jsonb_to_recordset(
		'[{"a":1,"b":2}, {"a":3,"b":4}]'::jsonb
	) as x(a int, b int);
