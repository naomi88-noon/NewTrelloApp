import pytest
from unittest.mock import Mock, MagicMock, patch
from app.repo.user_repo import UserRepo
from app.schema.user_schema import UserCreate, UserUpdate


@pytest.fixture
def user_repo():
    return UserRepo()


@pytest.fixture
def mock_db():
    return Mock()


@pytest.fixture
def mock_user():
    user = Mock()
    user.id = 1
    user.email = "test@example.com"
    user.name = "testuser"
    user.password = "qwerty"
    return user


class TestUserRepo:
    
    def test_create_user_success(self, user_repo, mock_db, mock_user):
        user_create = UserCreate(email="test@example.com", name="testuser", password="qwerty")
        mock_db.commit = Mock()
        mock_db.refresh = Mock()
        
        with patch.object(user_repo.model, '__call__', return_value=mock_user):
            result = user_repo.create_user(mock_db, user_create)
        
        mock_db.add.assert_called_once()
        mock_db.commit.assert_called_once()
        mock_db.refresh.assert_called_once()
    
    def test_get_all_users(self, user_repo, mock_db, mock_user):
        mock_db.query.return_value.all.return_value = [mock_user]
        
        result = user_repo.get_all_users(mock_db)
        
        assert result == [mock_user]
        mock_db.query.assert_called_once()
    
    def test_get_user_by_id_found(self, user_repo, mock_db, mock_user):
        mock_db.query.return_value.filter.return_value.first.return_value = mock_user
        
        result = user_repo.get_user_by_id(mock_db, 1)
        
        assert result == mock_user
    
    def test_get_user_by_id_not_found(self, user_repo, mock_db):
        mock_db.query.return_value.filter.return_value.first.return_value = None
        
        result = user_repo.get_user_by_id(mock_db, 999)
        
        assert result is None
    
    def test_update_user_success(self, user_repo, mock_db, mock_user):
        update_data = UserUpdate(name="testuser")
        user_repo.get_user_by_id = Mock(return_value=mock_user)
        mock_db.commit = Mock()
        mock_db.refresh = Mock()
        
        result = user_repo.update_user(mock_db, 1, update_data)
        
        mock_db.commit.assert_called_once()
    
    def test_update_user_not_found(self, user_repo, mock_db):
        update_data = UserUpdate(name="newname")
        user_repo.get_user_by_id = Mock(return_value=None)
        
        result = user_repo.update_user(mock_db, 999, update_data)
        
        assert result is None
    
    def test_delete_user_success(self, user_repo, mock_db, mock_user):
        user_repo.get_user_by_id = Mock(return_value=mock_user)
        mock_db.delete = Mock()
        mock_db.commit = Mock()
        
        result = user_repo.delete_user(mock_db, 1)
        
        mock_db.delete.assert_called_once_with(mock_user)
        mock_db.commit.assert_called_once()
        assert result is True
    
    def test_delete_user_not_found(self, user_repo, mock_db):
        user_repo.get_user_by_id = Mock(return_value=None)
        
        result = user_repo.delete_user(mock_db, 999)
        
        assert result is None