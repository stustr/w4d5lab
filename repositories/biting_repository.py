from db.run_sql import run_sql
from models.human import Human
from models.zombie import Zombie
from repositories import human_repository, zombie_repository
import pdb

def save(biting):
    
    sql = "INSERT INTO bitings (human_id, zombie_id) values (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    biting.id = id
    