select *
from vitalperiodic
where patientunitstayid in 
   (select patientunitstayid
   from admissiondx
   where (admitdxpath like '%deep vein%') or (admitdxpath like '%Embolus%'))
   AND
   (heartrate>110 or heartrate=110)
   AND
   observationoffset<1440
   