def test_nothing():
    assert breakupsearchstring('tag:inbox AND NOT tag:killed') == list()


def test_searchstring():
    assert breakupsearchstring('alot') == ['alot']


def test_mixed():
    assert breakupsearchstring('tag:unread notmuch') == ['notmuch']


def test_twosearchterms():
    assert breakupsearchstring('tag:unread notmuch alot') == ['notmuch', 'alot']
