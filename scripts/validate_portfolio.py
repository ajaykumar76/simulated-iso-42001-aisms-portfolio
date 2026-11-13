#!/usr/bin/env python3
"""Structural and cross-register checks for a simulated ISO/IEC 42001 portfolio."""
from __future__ import annotations
import argparse,csv,re,sys
from pathlib import Path
from urllib.parse import unquote
ROOT=Path(__file__).resolve().parents[1]
REQUIRED={"AI_System_Inventory_Template.csv","AI_Risk_Register_Template.csv","AI_Impact_Assessment_Template.csv","Risk_Treatment_Plan_Template.csv","Supplier_Register_Template.csv","Control_Evidence_Register_Template.csv","Audit_Findings_CAPA_Template.csv"}
EXPECTED={"03-AI-System-Inventory/AI_System_Inventory.csv":5,"04-AI-Risk-Assessment/AI_Risk_Assessment_Register.csv":10,"05-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv":8,"06-Risk-Treatment/AI_Risk_Treatment_Plan.csv":10,"08-Data-and-Supplier-Governance/AI_Data_and_Supplier_Register.csv":5,"09-Control-Mapping/ISO42001_Control_Mapping.csv":14,"10-Control-Evidence/AI_Control_Evidence_Tracker.csv":15,"11-Internal-Audit/AI_Internal_Audit_Checklist.csv":15,"11-Internal-Audit/AI_Audit_Findings_Register.csv":6,"11-Internal-Audit/AI_Audit_CAPA_Cross_Reference.csv":6,"12-NCR-CAPA/AI_NCR_CAPA_Register.csv":6,"13-Management-Review/AI_Management_Review_Action_Register.csv":6,"16-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv":8}
def read(path):
 try:
  with path.open(encoding="utf-8-sig",newline="") as f:return list(csv.DictReader(f)),None
 except (OSError,UnicodeError,csv.Error) as e:return [],str(e)
def main():
 ap=argparse.ArgumentParser();ap.add_argument("--require-source",action="store_true");args=ap.parse_args();issues=[]
 tdir=ROOT/"templates";present={p.name for p in tdir.glob("*.csv")} if tdir.exists() else set()
 for x in sorted(REQUIRED-present):issues.append("missing template: "+x)
 csvs=sorted(ROOT.rglob("*.csv"))
 for p in csvs:
  rows,e=read(p)
  if e:issues.append(f"{p.relative_to(ROOT)} unreadable: {e}");continue
  with p.open(encoding="utf-8-sig",newline="") as f:raw=list(csv.reader(f))
  if not raw or not raw[0] or any(not c.strip() for c in raw[0]):issues.append(f"{p.relative_to(ROOT)} has empty header")
  elif len({c.strip().casefold() for c in raw[0]})!=len(raw[0]):issues.append(f"{p.relative_to(ROOT)} has duplicate headers")
  for n,row in enumerate(raw[1:],2):
   if row and any(x.strip() for x in row) and len(row)!=len(raw[0]):issues.append(f"{p.relative_to(ROOT)}:{n} has inconsistent column count")
 readme=ROOT/"README.md"
 if not readme.is_file():issues.append("README.md missing")
 else:
  for raw in re.findall(r"!?\\[[^\\]]*\\]\\(([^)]+)\\)",readme.read_text(encoding="utf-8")):
   target=raw.strip().split()[0].strip("<>")
   if target and not target.startswith(("http://","https://","mailto:","#")):
    resolved=(ROOT/unquote(target.split("#",1)[0])).resolve()
    if not resolved.is_relative_to(ROOT.resolve()) or not resolved.exists():issues.append("invalid README link: "+raw)
 source=ROOT/"iso42001"
 if args.require_source and not source.is_dir():issues.append("iso42001 source folder missing")
 if source.is_dir():
  count=sum(p.is_file() for p in source.rglob("*"))
  if count<50:issues.append(f"source file count {count}; expected at least 50")
  regs={}
  for rel,n in EXPECTED.items():
   rows,e=read(source/rel);regs[rel]=rows
   if e:issues.append(f"{rel} unreadable: {e}")
   elif len(rows)!=n:issues.append(f"{rel}: expected {n} data rows, found {len(rows)}")
  risk=regs.get("04-AI-Risk-Assessment/AI_Risk_Assessment_Register.csv",[]);riskids={r.get("Risk ID") for r in risk}
  controls=regs.get("09-Control-Mapping/ISO42001_Control_Mapping.csv",[]);controlids={r.get("Control ID") for r in controls}
  findings=regs.get("11-Internal-Audit/AI_Audit_Findings_Register.csv",[]);findingids={r.get("Finding ID") for r in findings}
  for r in risk:
   try:
    l,i,s=int(r["Likelihood"]),int(r["Impact"]),int(r["Score"]);band="Low" if s<=4 else "Medium" if s<=9 else "High" if s<=15 else "Critical"
    if not(1<=l<=5 and 1<=i<=5) or s!=l*i:issues.append(f"{r.get('Risk ID')}: invalid score arithmetic or 1-5 inputs")
    if r.get("Rating")!=band:issues.append(f"{r.get('Risk ID')}: rating should be {band} under illustrative bands")
   except (KeyError,ValueError):issues.append(f"{r.get('Risk ID')}: invalid risk score")
  links=[("06-Risk-Treatment/AI_Risk_Treatment_Plan.csv","Risk ID",riskids),("05-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv","Related risk ID",riskids),("16-AI-Impact-Assessment/AI_Impact_Assessment_Register.csv","Related risk ID",riskids),("10-Control-Evidence/AI_Control_Evidence_Tracker.csv","Control ID",controlids),("11-Internal-Audit/AI_Internal_Audit_Checklist.csv","Control ID",controlids),("11-Internal-Audit/AI_Audit_CAPA_Cross_Reference.csv","Finding ID",findingids),("12-NCR-CAPA/AI_NCR_CAPA_Register.csv","Finding ID",findingids)]
  for rel,key,valid in links:
   for row in regs.get(rel,[]):
    v=row.get(key,"")
    if v and v not in valid:issues.append(f"{rel}: {key} {v} has no matching record")
 if issues:
  print("Validation failed:");[print("ERROR:",x) for x in issues];return 1
 print(f"CSV structure checks passed for {len(csvs)} CSV files.")
 print("Risk arithmetic, illustrative rating bands and selected cross-register references passed.")
 print("Passing checks do not establish implementation, evidence sufficiency, audit quality, legal compliance or ISO/IEC 42001 conformity.")
 return 0
if __name__=="__main__":sys.exit(main())
