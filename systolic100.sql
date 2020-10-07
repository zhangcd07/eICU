select *
from vitalperiodic
where patientunitstayid in 
   (select patientunitstayid
   from admissiondx
   where (admitdxpath like '%deep vein%') or (admitdxpath like '%Embolus%'))
   AND
   systemicsystolic<100
   AND
   observationoffset<1440