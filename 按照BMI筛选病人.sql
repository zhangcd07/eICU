select age, gender, patientunitstayid, unitdischargestatus, admissionweight/admissionheight/admissionheight*100*100 as BMI
from patient
where 
	(patientunitstayid in
   (
   select patientunitstayid
   from admissiondx
   where admitdxpath like '%Embolus%'))
	AND
	admissionheight>0
	AND 
	admissionweight/admissionheight/admissionheight*100*100 <100
	 AND admissionweight/admissionheight/admissionheight*100*100 >1

order by BMI desc
