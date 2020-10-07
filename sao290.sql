select *
from vitalperiodic
where patientunitstayid in 
   (select patientunitstayid
   from admissiondx
   where (admitdxpath like '%deep vein%') or (admitdxpath like '%Embolus%'))
   AND
   sao2<90
   AND
   observationoffset<1440