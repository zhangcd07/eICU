select patientunitstayid
from physicalexam
where 
	physicalexampath like '%Mental Status%'
	and
	(not physicalexamvalue in ('oriented x3', 'normal LOC', 'calm/appropriate', 'agitated at times'))