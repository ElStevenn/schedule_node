import time
import socket
import redis
import schedule
import httpx
import json
import os
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, Union, Literal, TypedDict, List
import pytz

class FoundingRate(TypedDict):
    symbol: str
    fundingRate: float # New Founding Rate

class BotHistoricalPNL(TypedDict):
    # Important Data
    id: str
    symbol: str
    operation_datetime: datetime

    # Secondary Data
    pnl: str
    avg_entry_price: str
    side: Literal['long', 'short']
    closed_value: str

    # Irelevant data
    opening_fee: str
    closing_fee: str
    net_profits: str
    
    

class RedisService:
    def __init__(self):
        hostname = socket.gethostname()
            
        if hostname == 'ip-172-31-3-153':  
            redis_host = 'redis_tasks'
            port = '6378'
        else:
            redis_host = 'localhost'
            port = '6379'

        self._r = redis.Redis(host='localhost', port='6378', decode_responses=True)
        self.ensure_correct_key_type()

    def ensure_correct_key_type(self):
        """Ensure the 'tasks' key is a hash or delete it if not."""
        if self._r.exists("tasks") and self._r.type("tasks") != "hash":
            print(f"Deleting the incorrect 'tasks' key of type {self._r.type('tasks')}.")
            self._r.delete("tasks")

    def save_task(self, task_id: str, task_data: Dict[str, Any]) -> None:
        """Save a task to Redis as a hash entry."""
        self.ensure_correct_key_type()
        self._r.hset("tasks", task_id, json.dumps(task_data))
        print(f"Task '{task_id}' saved successfully.")

    def get_task(self, task_id: str) -> Optional[Dict[str, Any]]:
        """Retrieve a task from Redis by its ID."""
        task_data = self._r.hget("tasks", task_id)
        if task_data:
            return json.loads(task_data)
        else:
            print(f"Task '{task_id}' not found.")
            return None

    def delete_task(self, task_id: str) -> None:
        """Delete a task from Redis."""
        result = self._r.hdel("tasks", task_id)
        if result:
            print(f"Task '{task_id}' deleted successfully.")
        else:
            print(f"Task '{task_id}' not found or could not be deleted.")

    def get_all_tasks(self) -> Dict[str, Any]:
        """Retrieve all tasks from Redis."""
        self.ensure_correct_key_type()
        tasks = self._r.hgetall("tasks")
        return {task_id: json.loads(task_data) for task_id, task_data in tasks.items()}

    def delete_all(self) -> None:
        """Delete all tasks in Redis."""
        self._r.delete("tasks")
        print("All tasks have been deleted from Redis.")

    """
        READ & WRITE & UPDATE $ DELETE for founding rate sercice
    """
    def add_new_crypto_lead(self, symbol: str, fundingRate: Union[float, int]) -> None:
        """Add a new crypto lead to Redis."""
        self.ensure_correct_key_type()
        crypto_lead_key = f"crypto_leads:{symbol}"
        crypto_lead_data = {"symbol": symbol, "fundingRate": fundingRate}
        self._r.hset("crpto_leads", crypto_lead_key, json.dumps(crypto_lead_data))
    
    def read_all_crypto_lead(self) -> Dict[str, Any]:
        """Read all crypto leads from Redis."""
        self.ensure_correct_key_type()
        crypto_leads = self._r.hgetall("crypto_leads")
        return [json.loads(data[1]) for data in crypto_leads.items()]



    def delete_all_crypto_leads(self) -> None:
        """Delete all crypto leads in Redis."""
        self._r.delete("crypto_leads")


    """
    READ & WRITE & UPDATE % DELETE to save the historical PNL
    """

    def add_new_pnl(self, data: BotHistoricalPNL):
        """Add a new PNL record to Redis."""
        self.ensure_correct_key_type()
        pnl_key = f"historical_pnl:{data['id']}"
        self._r.hset("historical_pnl", pnl_key, json.dumps(data, default=str))

    
    def delete_30_days_pnl(self):
        """Delete PNL records older than 30 days."""
        cutoff_date = datetime.now(pytz.utc) - timedelta(days=30)
        all_pnls = self._r.hgetall("historical_pnl")

        for pnl_key, pnl_data in all_pnls.items():
            pnl_record = json.loads(pnl_data)
            operation_datetime = datetime.fromisoformat(pnl_record['operation_datetime'])
            if operation_datetime < cutoff_date:
                self._r.hdel("historical_pnl", pnl_key)


        
if __name__ == "__main__":
    redis_service = RedisService()

    # Define a task with a unique ID
    task_id = "task_1"
    task_data = {
        "url": "http://example.com/api/notify",
        "method": "post",
        "data": {"message": "Hello World"},
        "headers": {"Content-Type": "application/json"},
        "execute_at": "12:00",
        "timezone": "Europe/Amsterdam"
    }

    # Save the task to Redis
    # redis_service.save_task(task_id, task_data)
    # print(redis_service.read_all_crypto_lead())
    # print(redis_service.delete_all_crypto_leads())


    # FOUNDING RATE 
    redis_service.swap_new_founding_rate("")
