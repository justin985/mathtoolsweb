from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import re

app = Flask(__name__)
CORS(app)
M2_PATH = "/usr/bin/M2"  # 你的 M2 絕對路徑

#M2_PATH = "/opt/homebrew/bin/M2"  # 你的 M2 絕對路徑

def run_sos(poly):
    # 清理輸入
    poly = poly.strip()
    if not poly:
        return {"error": "Empty expression"}
    
    # 檢查基本語法
    if not all(c.isalnum() or c.isspace() or c in '+-*/()^,' for c in poly):
        return {"error": "Invalid characters in expression"}

    script = f"""
needsPackage ("SumsOfSquares");
R = QQ[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z];
f = ({poly});
result = sosPoly solveSOS f;
print toString result;
"""
    try:
        result = subprocess.run(
            [M2_PATH, "--no-readline"],
            input=script.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10
        )
        
        stderr = result.stderr.decode("utf-8").strip()
        output = result.stdout.decode("utf-8")
        output = output.replace("\r", "").replace("\n", " ").strip()
        
        # 如果有輸出結果，即使有版本信息也返回
        if output:
            return {"output": output, "error": stderr if stderr else None}
            
        # 如果沒有輸出但有錯誤信息
        if stderr:
            return {"error": f"M2 error:{stderr}"}
            
        # 如果既沒有輸出也沒有錯誤信息
        if result.returncode != 0:
            return {"error": "Unknown error in M2 calculation"}
            
        return {"error": "No output from M2"}
        
    except subprocess.TimeoutExpired:
        return {"error": "Computation timeout after 10 seconds"}
    except Exception as e:
        return {"error": str(e)}

@app.route('/sos', methods=['POST'])
def handle_sos():
    data = request.get_json()
    if not data or 'expr' not in data:
        return jsonify({"error": "Missing expression"})
    return jsonify(run_sos(data['expr']))

if __name__ == '__main__':
    # 生產環境設定
    app.run(host='0.0.0.0', port=5000, debug=False)
