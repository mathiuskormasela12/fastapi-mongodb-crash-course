# ========== Main ==========
# import all packages
import imp
import uvicorn
from app.config.config import PORT

if __name__ == '__main__' :
	uvicorn.run('app.app:app', host='127.0.0.1', port=PORT, reload=True)