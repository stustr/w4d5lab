from db.run_sql import run_sql
from models.human import Human
from models.zombie import Zombie
from models.biting import Biting
from repositories import human_repository, zombie_repository
import pdb


def save(biting):

    sql = "INSERT INTO bitings (human_id, zombie_id) values (%s, %s) RETURNING id"
    values = [biting.human.id, biting.zombie.id]
    results = run_sql(sql, values)
    id = results[0]["id"]
    biting.id = id


def select_all():
    bitings = []
    sql = "SELECT * FROM bitings"
    results = run_sql(sql)

    for result in results:
        human = human_repository.select(result["human_id"])
        zombie = zombie_repository.select(result["zombie_id"])
        biting = Biting(human.name, zombie.name, result["id"])
        bitings.append(biting)
    return bitings

def select(id):
    sql = "SELECT * FROM bitings WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    
    if results:
        result = results[0]
        human = human_repository.select(result["human_id"])
        zombie = zombie_repository.select(result["zombie_id"])
        biting = Biting(human.name, zombie.name, result["id"])
    return biting

def delete(id):
    sql = "DELETE FROM bitings WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    
def delete_all():
    sql = "DELETE FROM bitings"
    run_sql(sql)
    
def update(biting):
     sql = "UPDATE bitings SET (human_id, zombie_id) = (%s, %s) WHERE id = %s"
     values = [biting.human.id, biting.zombie.id, biting.id]
     run_sql(sql, values)
     