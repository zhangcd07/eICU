select *
from vitalperiodic
where patientunitstayid in 
   (select patientunitstayid
   from admissiondx
   where (admitdxpath like '%deep vein%') or (admitdxpath like '%Embolus%'))
   AND
   (respiration>30 or respiration=30)
   AND
   observationoffset<1440