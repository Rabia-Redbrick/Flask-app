
import app from app
import db,models from app


u = models.User(nickname='john', email='john@email.com')
db.session.add(u)
db.session.commit()