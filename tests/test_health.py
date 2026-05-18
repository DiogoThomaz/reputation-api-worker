def test_health_ok():
    from reputation_api_worker.app import health

    assert health() is True