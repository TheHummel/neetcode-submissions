class LRUCache {
private:
    using Pair = std::pair<int, int>; 
    using List = std::list<Pair>;

public:
    int capacity;
    List cache;
    std::unordered_map<int,List::iterator> cacheMap;

    LRUCache(int _capacity) {
        capacity = _capacity;
    }
    
    int get(int key) {
        if (cacheMap.find(key) == cacheMap.end()) return -1;
        List::iterator it = cacheMap[key];
        cache.splice(cache.begin(), cache, it);

        return it->second;
        
    }
    
    void put(int key, int value) {
        if (cacheMap.find(key) != cacheMap.end()) {
            List::iterator it = cacheMap[key];
            it->second = value;
            cache.splice(cache.begin(), cache, it);
        } else {
            if (cache.size() >= capacity) {
                // evict
                List::iterator it_lru = std::prev(cache.end());
                cacheMap.erase(it_lru->first);
                cache.pop_back();
            }
            List::iterator it = cache.insert(cache.begin(), {key, value});
            cacheMap[key] = it;
        }
        
    }
};
