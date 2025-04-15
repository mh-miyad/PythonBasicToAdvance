"""
Web Learner Module

This module learns from the internet by searching for code examples,
documentation, and best practices.
"""

import os
import re
import json
import time
import random

# Try to import optional dependencies
try:
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import quote_plus
    DEPENDENCIES_AVAILABLE = True
except ImportError:
    DEPENDENCIES_AVAILABLE = False
    print("Warning: Some dependencies are missing for the WebLearner module.")
    print("To enable all features, install the required dependencies:")
    print("pip install beautifulsoup4 requests")

class WebLearner:
    """Learns from the internet by searching for code examples and documentation"""

    def __init__(self):
        """Initialize the web learner"""
        self.cache_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'cache')
        os.makedirs(self.cache_dir, exist_ok=True)

        self.dependencies_available = DEPENDENCIES_AVAILABLE
        if not self.dependencies_available:
            print("WebLearner initialized with limited functionality due to missing dependencies.")
            return

        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        ]

    def search_code_examples(self, query, language=None, limit=5):
        """Search for code examples related to the query"""
        if not self.dependencies_available:
            print("Cannot search code examples: required dependencies not installed.")
            return []

        # Add language to the query if provided
        if language:
            query = f"{query} {language} example"
        else:
            query = f"{query} example"

        # Check cache first
        cache_key = self._get_cache_key(query)
        cached_results = self._get_from_cache(cache_key)

        if cached_results:
            print(f"Using cached results for query: {query}")
            return cached_results

        print(f"Searching for code examples: {query}")

        # Search for code examples
        examples = []

        try:
            # Try to get examples from GitHub
            github_examples = self._search_github(query, limit)
            examples.extend(github_examples)

            # If we need more examples, try Stack Overflow
            if len(examples) < limit:
                stackoverflow_examples = self._search_stackoverflow(query, limit - len(examples))
                examples.extend(stackoverflow_examples)

            # Cache the results
            self._save_to_cache(cache_key, examples)

            return examples
        except Exception as e:
            print(f"Error searching for code examples: {e}")
            return []

    def search_documentation(self, topic, framework=None, limit=3):
        """Search for documentation related to the topic"""
        if not self.dependencies_available:
            print("Cannot search documentation: required dependencies not installed.")
            return []

        # Add framework to the query if provided
        if framework:
            query = f"{topic} {framework} documentation"
        else:
            query = f"{topic} documentation"

        # Check cache first
        cache_key = self._get_cache_key(query)
        cached_results = self._get_from_cache(cache_key)

        if cached_results:
            print(f"Using cached results for query: {query}")
            return cached_results

        print(f"Searching for documentation: {query}")

        # Search for documentation
        docs = []

        try:
            # Try to get documentation from MDN for web topics
            if any(keyword in topic.lower() for keyword in ['html', 'css', 'javascript', 'js', 'web']):
                mdn_docs = self._search_mdn(topic, limit)
                docs.extend(mdn_docs)

            # If we need more docs, try a general search
            if len(docs) < limit:
                general_docs = self._general_search(query, limit - len(docs))
                docs.extend(general_docs)

            # Cache the results
            self._save_to_cache(cache_key, docs)

            return docs
        except Exception as e:
            print(f"Error searching for documentation: {e}")
            return []

    def get_bootstrap_example(self, component):
        """Get an example of a Bootstrap component"""
        if not self.dependencies_available:
            print("Cannot get Bootstrap examples: required dependencies not installed.")
            return None

        # Check cache first
        cache_key = self._get_cache_key(f"bootstrap_{component}")
        cached_results = self._get_from_cache(cache_key)

        if cached_results and len(cached_results) > 0:
            print(f"Using cached Bootstrap example for: {component}")
            return cached_results[0]

        print(f"Searching for Bootstrap example: {component}")

        try:
            # Try to get an example from the Bootstrap documentation
            url = f"https://getbootstrap.com/docs/5.1/components/{component}/"

            headers = {
                'User-Agent': random.choice(self.user_agents)
            }

            response = requests.get(url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for code examples
            examples = []

            # Find all code blocks
            code_blocks = soup.select('div.highlight')

            for block in code_blocks:
                code = block.get_text()
                if code.strip():
                    examples.append({
                        'title': f"Bootstrap {component} example",
                        'code': code.strip(),
                        'language': 'html',
                        'source': url
                    })

            # Cache the results
            self._save_to_cache(cache_key, examples)

            return examples[0] if examples else None
        except Exception as e:
            print(f"Error getting Bootstrap example: {e}")
            return None

    def _search_github(self, query, limit=3):
        """Search for code examples on GitHub"""
        examples = []

        try:
            # GitHub search URL
            search_url = f"https://github.com/search?q={quote_plus(query)}&type=code"

            headers = {
                'User-Agent': random.choice(self.user_agents)
            }

            response = requests.get(search_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Find code snippets
            code_blocks = soup.select('div.code-block')

            for block in code_blocks[:limit]:
                # Extract code and metadata
                code = block.select_one('pre').get_text() if block.select_one('pre') else ""
                repo_link = block.select_one('a.Link--secondary')
                repo_name = repo_link.get_text() if repo_link else "Unknown repository"
                file_link = block.select_one('a.Link--primary')
                file_path = file_link.get_text() if file_link else "Unknown file"

                if code.strip():
                    examples.append({
                        'title': f"{repo_name} - {file_path}",
                        'code': code.strip(),
                        'language': self._detect_language(file_path),
                        'source': f"https://github.com{file_link['href']}" if file_link and 'href' in file_link.attrs else search_url
                    })

            # Add a delay to avoid rate limiting
            time.sleep(random.uniform(1, 2))

            return examples
        except Exception as e:
            print(f"Error searching GitHub: {e}")
            return []

    def _search_stackoverflow(self, query, limit=3):
        """Search for code examples on Stack Overflow"""
        examples = []

        try:
            # Stack Overflow search URL
            search_url = f"https://stackoverflow.com/search?q={quote_plus(query)}"

            headers = {
                'User-Agent': random.choice(self.user_agents)
            }

            response = requests.get(search_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Find question links
            question_links = soup.select('a.s-link')

            for link in question_links[:limit]:
                if 'href' in link.attrs and '/questions/' in link['href']:
                    question_url = f"https://stackoverflow.com{link['href']}"

                    # Get the question page
                    question_response = requests.get(question_url, headers=headers)
                    question_response.raise_for_status()

                    question_soup = BeautifulSoup(question_response.text, 'html.parser')

                    # Find accepted or top answer
                    answer = question_soup.select_one('div.accepted-answer') or question_soup.select_one('div.answer')

                    if answer:
                        # Find code blocks in the answer
                        code_blocks = answer.select('pre code')

                        for block in code_blocks:
                            code = block.get_text()
                            if code.strip():
                                # Try to detect the language
                                language = block.get('class', [''])[0] if block.get('class') else ''
                                if language.startswith('lang-'):
                                    language = language[5:]
                                else:
                                    language = self._detect_language_from_code(code)

                                examples.append({
                                    'title': link.get_text(),
                                    'code': code.strip(),
                                    'language': language,
                                    'source': question_url
                                })

                    # Add a delay to avoid rate limiting
                    time.sleep(random.uniform(1, 2))

            return examples
        except Exception as e:
            print(f"Error searching Stack Overflow: {e}")
            return []

    def _search_mdn(self, topic, limit=3):
        """Search for documentation on MDN"""
        docs = []

        try:
            # MDN search URL
            search_url = f"https://developer.mozilla.org/en-US/search?q={quote_plus(topic)}"

            headers = {
                'User-Agent': random.choice(self.user_agents)
            }

            response = requests.get(search_url, headers=headers)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            # Find search results
            results = soup.select('a.result-title')

            for result in results[:limit]:
                if 'href' in result.attrs:
                    doc_url = f"https://developer.mozilla.org{result['href']}"

                    # Get the documentation page
                    doc_response = requests.get(doc_url, headers=headers)
                    doc_response.raise_for_status()

                    doc_soup = BeautifulSoup(doc_response.text, 'html.parser')

                    # Extract the main content
                    content = doc_soup.select_one('article')

                    if content:
                        # Extract text and code examples
                        text = content.get_text()
                        code_blocks = content.select('pre')

                        code_examples = []
                        for block in code_blocks:
                            code = block.get_text()
                            if code.strip():
                                code_examples.append(code.strip())

                        docs.append({
                            'title': result.get_text(),
                            'url': doc_url,
                            'summary': text[:500] + '...' if len(text) > 500 else text,
                            'code_examples': code_examples
                        })

                    # Add a delay to avoid rate limiting
                    time.sleep(random.uniform(1, 2))

            return docs
        except Exception as e:
            print(f"Error searching MDN: {e}")
            return []

    def _general_search(self, query, limit=3):
        """Perform a general search for documentation"""
        docs = []

        try:
            # This is a simplified implementation
            # In a real implementation, you would use a search API or scrape search results

            # For now, we'll just return some placeholder results
            docs = [
                {
                    'title': f"Documentation for {query}",
                    'url': f"https://example.com/docs/{query.replace(' ', '-')}",
                    'summary': f"This is a placeholder summary for {query}.",
                    'code_examples': []
                }
            ]

            return docs[:limit]
        except Exception as e:
            print(f"Error performing general search: {e}")
            return []

    def _detect_language(self, file_path):
        """Detect the programming language from a file path"""
        _, ext = os.path.splitext(file_path)
        ext = ext.lower()

        if ext in ['.html', '.htm']:
            return 'html'
        elif ext in ['.css', '.scss', '.sass', '.less']:
            return 'css'
        elif ext in ['.js', '.jsx']:
            return 'javascript'
        elif ext in ['.ts', '.tsx']:
            return 'typescript'
        elif ext == '.py':
            return 'python'
        elif ext in ['.java', '.kt']:
            return 'java'
        elif ext in ['.c', '.cpp', '.h', '.hpp']:
            return 'c++'
        elif ext == '.cs':
            return 'csharp'
        elif ext == '.go':
            return 'go'
        elif ext == '.rb':
            return 'ruby'
        elif ext == '.php':
            return 'php'
        elif ext == '.swift':
            return 'swift'
        elif ext in ['.json', '.xml', '.yml', '.yaml']:
            return ext[1:]
        else:
            return 'unknown'

    def _detect_language_from_code(self, code):
        """Detect the programming language from code content"""
        # This is a very simplified implementation
        # In a real implementation, you would use more sophisticated techniques

        code = code.strip()

        if re.search(r'<\w+[^>]*>.*?</\w+>', code, re.DOTALL):
            return 'html'
        elif re.search(r'[\w-]+\s*:\s*[^;]+;', code):
            return 'css'
        elif re.search(r'function\s+\w+\s*\(', code) or re.search(r'var\s+\w+\s*=', code) or re.search(r'const\s+\w+\s*=', code):
            return 'javascript'
        elif re.search(r'import\s+.*\s+from\s+', code) or re.search(r'export\s+(default\s+)?', code):
            return 'javascript'
        elif re.search(r'class\s+\w+\s*{', code) or re.search(r'interface\s+\w+\s*{', code):
            return 'typescript'
        elif re.search(r'def\s+\w+\s*\(', code) or re.search(r'import\s+\w+', code):
            return 'python'
        else:
            return 'unknown'

    def _get_cache_key(self, query):
        """Generate a cache key from a query"""
        # Remove special characters and convert to lowercase
        key = re.sub(r'[^a-zA-Z0-9]', '_', query.lower())
        # Truncate if too long
        if len(key) > 100:
            key = key[:100]
        return key

    def _get_from_cache(self, key):
        """Get results from cache"""
        cache_file = os.path.join(self.cache_dir, f"{key}.json")

        if os.path.exists(cache_file):
            try:
                with open(cache_file, 'r') as f:
                    data = json.load(f)

                # Check if the cache is still valid (less than 1 day old)
                if time.time() - data['timestamp'] < 86400:  # 24 hours
                    return data['results']
            except Exception as e:
                print(f"Error reading from cache: {e}")

        return None

    def _save_to_cache(self, key, results):
        """Save results to cache"""
        cache_file = os.path.join(self.cache_dir, f"{key}.json")

        try:
            with open(cache_file, 'w') as f:
                json.dump({
                    'timestamp': time.time(),
                    'results': results
                }, f, indent=2)
        except Exception as e:
            print(f"Error saving to cache: {e}")

    def clear_cache(self):
        """Clear the cache"""
        for file in os.listdir(self.cache_dir):
            if file.endswith('.json'):
                os.remove(os.path.join(self.cache_dir, file))
