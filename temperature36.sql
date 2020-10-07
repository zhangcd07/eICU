select *
from vitalperiodic
where patientunitstayid in 
   (select patientunitstayid
   from admissiondx
   where (admitdxpath like '%deep vein%') or (admitdxpath like '%Embolus%'))
   AND
   observationoffset<1440
   AND ((temperature<96.8 AND temperature >50) OR (temperature<36))