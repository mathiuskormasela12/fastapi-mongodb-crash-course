# ========== User Routes ==========
# import all packages
from urllib import response
from bson import ObjectId
from fastapi import APIRouter, Response, status
from app.models.user import User
from app.config.db import conn 
from app.schemas.user import usersEntity

user = APIRouter()

@user.get('/api/v1/users', tags=['users'], status_code=200)
async def get_all_users(response: Response) :
	results: usersEntity = usersEntity(conn.fastapi.user.find())

	if len(results) < 1 :
		response.status_code = status.HTTP_404_NOT_FOUND
		return {
			'message': 'The users are empty',
			'results': results
		}
	else :
		return {
			'message': 'Success to get all users',
			'results': results,
		}

@user.get('/api/v1/users/{id}', tags=['users'], status_code=200)
async def get_user(id: str, response: Response) :
	try :
		results = usersEntity(conn.fastapi.user.find({
			'_id': ObjectId(id)
		}))

		if len(results) < 1 :
			response.status_code = status.HTTP_404_NOT_FOUND
			return {
				'message': f'The user with id {id} does not exists',
				'results': results
			}
		else :
			return {
				'message': f'Success to get user with id {id}',
				'results': results[0],
			}
	except :
		response.status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
		return {
			'message': 'Server Error'
		}

@user.post('/api/v1/users', tags=['users'], status_code=201)
async def create_user(body: User) -> dict:
	conn.fastapi.user.insert_one(dict(body))
	return {
		'message': 'A new user was created',
	}

@user.put('/api/v1/users/{id}', tags=['users'], status_code=200) 
async def update_user(id: str, body: User, response: Response) -> dict :
	isExists = conn.fastapi.user.find({
		'_id': ObjectId(id),
	})
	if len(list(isExists)) < 1 :
		response.status_code=status.HTTP_404_NOT_FOUND
		return {
			'message': f'The user with id {id} was not found'
		}
	
	try :
		conn.fastapi.user.update_one({
		'_id': ObjectId(id)
		}, {
			'$set': dict(body)
		})
		return {
			'message': 'The use was updated successfully'
		}
	except :
		response.status_code=status.HTTP_400_BAD_REQUEST
		return {
			'message': 'Failed to update the user'
		}

@user.delete('/api/v1/users/{id}', tags=['users'], status_code=200) 
async def update_user(id: str, response: Response) -> dict :
	isExists = conn.fastapi.user.find({
		'_id': ObjectId(id),
	})
	if len(list(isExists)) < 1 :
		response.status_code=status.HTTP_404_NOT_FOUND
		return {
			'message': f'The user with id {id} was not found'
		}
	
	try :
		conn.fastapi.user.delete_one({
		'_id': ObjectId(id)
		})
		return {
			'message': 'The use was deleted successfully'
		}
	except :
		response.status_code=status.HTTP_400_BAD_REQUEST
		return {
			'message': 'Failed to delete the user'
		}
