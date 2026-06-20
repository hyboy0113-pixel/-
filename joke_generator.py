"""
랜덤 Joke 생성기 - Python 버전
JokeAPI를 사용하여 랜덤 joke를 가져옵니다.
"""

import requests
import json
from typing import Dict, Optional


class JokeGenerator:
    """JokeAPI를 사용하는 Joke 생성기 클래스"""
    
    def __init__(self):
        self.api_url = "https://v2.jokeapi.dev/joke/Any"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def get_joke(self, joke_type: str = "single") -> Optional[Dict]:
        """
        API에서 joke를 가져옵니다.
        
        Args:
            joke_type: "single" (한 줄) 또는 "twopart" (투 파트)
        
        Returns:
            Joke 데이터 딕셔너리 또는 None
        """
        try:
            params = {"type": joke_type}
            response = requests.get(self.api_url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get("error"):
                print("❌ API 오류:", data.get("message"))
                return None
            
            return data
            
        except requests.exceptions.Timeout:
            print("❌ 오류: 요청 시간 초과. 다시 시도해주세요.")
            return None
        except requests.exceptions.ConnectionError:
            print("❌ 오류: 인터넷 연결을 확인해주세요.")
            return None
        except requests.exceptions.RequestException as e:
            print(f"❌ API 요청 오류: {e}")
            return None
    
    def display_joke(self, joke_data: Dict) -> None:
        """
        Joke 데이터를 멋지게 표시합니다.
        
        Args:
            joke_data: API에서 받은 joke 데이터
        """
        print("\n" + "="*60)
        
        if joke_data["type"] == "single":
            print(f"😂 {joke_data['joke']}")
        else:
            print(f"🎭 {joke_data['setup']}")
            print(f"💬 {joke_data['delivery']}")
        
        print(f"\n📂 유형: {joke_data['type']}")
        print(f"🏷️  카테고리: {', '.join(joke_data['category'].split(','))}")
        print("="*60 + "\n")
    
    def run_interactive(self) -> None:
        """
        대화형 모드로 실행합니다.
        """
        print("\n" + "🎉 "*10)
        print("  랜덤 Joke 생성기 (Python 버전)")
        print("🎉 "*10 + "\n")
        
        while True:
            print("메뉴:")
            print("1. 새로운 Joke 가져오기")
            print("2. 한 줄 Joke만 가져오기")
            print("3. 투 파트 Joke만 가져오기")
            print("4. 종료")
            
            choice = input("\n선택 (1-4): ").strip()
            
            if choice == "1":
                joke = self.get_joke()
                if joke:
                    self.display_joke(joke)
            
            elif choice == "2":
                joke = self.get_joke("single")
                if joke:
                    self.display_joke(joke)
            
            elif choice == "3":
                joke = self.get_joke("twopart")
                if joke:
                    self.display_joke(joke)
            
            elif choice == "4":
                print("👋 프로그램을 종료합니다. 안녕히 가세요!")
                break
            
            else:
                print("❌ 잘못된 선택입니다. 다시 시도해주세요.")
    
    def get_multiple_jokes(self, count: int = 5) -> None:
        """
        여러 개의 Joke를 한 번에 가져옵니다.
        
        Args:
            count: 가져올 joke의 개수
        """
        print(f"\n🎯 {count}개의 Joke를 가져오는 중...\n")
        
        jokes = []
        for i in range(count):
            joke = self.get_joke()
            if joke:
                jokes.append(joke)
                print(f"✅ {i+1}/{count} 완료")
        
        print("\n" + "="*60)
        print(f"✨ 총 {len(jokes)}개의 Joke를 가져왔습니다!")
        print("="*60 + "\n")
        
        for idx, joke_data in enumerate(jokes, 1):
            print(f"\n[Joke #{idx}]")
            self.display_joke(joke_data)


def main():
    """메인 함수"""
    generator = JokeGenerator()
    
    print("\n💡 사용 예제:\n")
    
    # 예제 1: 단일 Joke 가져오기
    print("1️⃣  단일 Joke 가져오기:")
    print("-" * 60)
    joke = generator.get_joke()
    if joke:
        generator.display_joke(joke)
    
    # 예제 2: 여러 개의 Joke 가져오기
    print("\n2️⃣  여러 개의 Joke 가져오기:")
    print("-" * 60)
    generator.get_multiple_jokes(3)
    
    # 예제 3: 대화형 모드 시작
    print("\n3️⃣  대화형 모드 시작:")
    print("-" * 60)
    user_input = input("대화형 모드를 시작하시겠습니까? (y/n): ").strip().lower()
    if user_input == 'y':
        generator.run_interactive()


if __name__ == "__main__":
    # requests 라이브러리 설치 확인
    try:
        import requests
    except ImportError:
        print("❌ 오류: 'requests' 라이브러리가 설치되지 않았습니다.")
        print("다음 명령어로 설치해주세요:")
        print("  pip install requests")
        exit(1)
    
    # 메인 함수 실행
    main()