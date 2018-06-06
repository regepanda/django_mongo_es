index_mappings = {
  "settings": {
    "analysis": {
      "analyzer": {
        "ik": {
            "tokenizer": "ik_max_word"
        }
      }
    }
  },
  "mappings": {
    "tour_product": {
      "dynamic": True,
      "properties": {
        "product_id": {"type": "integer"},
        "provider_id": {"type": "integer"},
        "is_published": {"type": "integer"},
        "is_deleted": {"type": "integer"},
        "created_at": {"type": "integer"},
        "updated_at": {"type": "integer"},
        "provider_code": {"type": "string"},
        "code": {"type": "string"},
        "subcode": {"type": "string"},
        "name": {"type": "string", "analyzer": "ik_max_word", "search_analyzer": "ik_max_word"},
        "name_provider": {"type": "string"},
        "image_url": {"type": "string"},
        "thumbnail_url": {"type": "string"},
        "map_image_url": {"type": "string"},
        "video_url": {"type": "string"},
        "advertised_price": {"type": "string"},
        "departure_city": {"type": "string"},
        "return_city": {"type": "string"},
      }
    }
  }
}

test_mappings = {
  "settings": {
    "analysis": {
      "analyzer": {
        "ik": {
            "tokenizer": "ik_max_word"
        }
      }
    }
  },
  "mappings": {
    "people": {
      "dynamic": True,
      "properties": {
        "name": {"type": "string", "analyzer": "ik_max_word", "search_analyzer": "ik_max_word"},
        "age": {"type": "integer"},
        "sex": {"type": "string"}
      }
    }
  }
}

