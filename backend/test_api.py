"""
Simple test script to verify API endpoints work correctly.
Run this script after starting the backend server with: uvicorn main:app --reload
"""
import requests
import json

BASE_URL = "http://localhost:8000"

def test_battery_status():
    """Test the /battery/status endpoint"""
    response = requests.get(f"{BASE_URL}/battery/status")
    if response.status_code == 200:
        data = response.json()
        print("✅ Battery Status endpoint working")
        print(f"   SOC: {data['SOC']}%, Voltage: {data['Voltage']}V, Current: {data['Current']}A")
        print(f"   Load: {data['Load']}kW, PV: {data['PV']}kW")
        return True
    else:
        print(f"❌ Battery Status endpoint failed: {response.status_code}")
        return False

def test_battery_logs():
    """Test the /battery/logs endpoint"""
    response = requests.get(f"{BASE_URL}/battery/logs")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Battery Logs endpoint working ({len(data)} records)")
        return True
    else:
        print(f"❌ Battery Logs endpoint failed: {response.status_code}")
        return False

def test_battery_recommendations():
    """Test the /battery/recommendations endpoint"""
    response = requests.get(f"{BASE_URL}/battery/recommendations")
    if response.status_code == 200:
        data = response.json()
        print("✅ Battery Recommendations endpoint working")
        print(f"   Time: {data['Time']}, SOC: {data['SOC']}%, Load: {data['Load']}kW, PV: {data['PV']}kW")
        print(f"   Recommendations:")
        for rec in data['Recs']:
            print(f"     - {rec}")
        return True
    else:
        print(f"❌ Battery Recommendations endpoint failed: {response.status_code}")
        return False

if __name__ == "__main__":
    print("Testing Battery Admin API endpoints...")
    print("-" * 60)
    
    try:
        results = []
        results.append(test_battery_status())
        print()
        results.append(test_battery_logs())
        print()
        results.append(test_battery_recommendations())
        print("-" * 60)
        
        if all(results):
            print("✅ All API endpoints working correctly!")
        else:
            print("❌ Some API endpoints failed")
            
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to server. Make sure the backend is running:")
        print("   cd backend && uvicorn main:app --reload")
