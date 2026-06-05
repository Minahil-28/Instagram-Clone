"""
DSA-Based Social Media Application
A comprehensive social media platform built entirely using custom data structures and algorithms.
Suitable as a semester project for Data Structures & Algorithms course.

Requirements: customtkinter, Pillow
Install: pip install customtkinter pillow
"""

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import json
import os
from datetime import datetime
from typing import Optional, List, Dict, Any
import hashlib

# ===================== THEME CONFIGURATION =====================
class Theme:
    """Centralized theme management with easy customization"""
    # Instagram-inspired Colors
    PRIMARY = "#E1306C"  # Instagram Pink
    SECONDARY = "#833AB4"  # Instagram Purple
    TERTIARY = "#F77737"  # Instagram Orange
    GRADIENT_START = "#833AB4"  # Purple
    GRADIENT_MID = "#C13584"  # Pink-Purple
    GRADIENT_END = "#E1306C"  # Pink
    
    BACKGROUND_DARK = "#000000"  # Pure black
    BACKGROUND_LIGHT = "#1a1a1a"  # Slightly lighter black
    CARD_BG = "#262626"  # Dark gray
    TEXT_PRIMARY = "#ffffff"
    TEXT_SECONDARY = "#b3b3b3"
    BUTTON_HOVER = "#C13584"  # Pink-Purple
    
    # Fonts
    FONT_FAMILY = "Segoe UI"
    FONT_TITLE = (FONT_FAMILY, 24, "bold")
    FONT_HEADING = (FONT_FAMILY, 18, "bold")
    FONT_SUBHEADING = (FONT_FAMILY, 14, "bold")
    FONT_BODY = (FONT_FAMILY, 12)
    FONT_SMALL = (FONT_FAMILY, 10)
    FONT_LOGO = ("Segoe Script", 32, "bold")  # For logo
    
    # Styling
    CORNER_RADIUS = 15
    BUTTON_CORNER_RADIUS = 12
    PADDING = 15

# ===================== CUSTOM DATA STRUCTURES =====================

class Node:
    """Generic node for linked lists"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None  # For doubly linked list

class LinkedList:
    """Doubly Linked List implementation"""
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        """Add element at the end"""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
    
    def prepend(self, data):
        """Add element at the beginning"""
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def delete(self, data):
        """Delete first occurrence of data"""
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                
                self.size -= 1
                return True
            current = current.next
        return False
    
    def find(self, condition):
        """Find element matching condition"""
        current = self.head
        while current:
            if condition(current.data):
                return current.data
            current = current.next
        return None
    
    def to_list(self):
        """Convert to Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def __len__(self):
        return self.size

class Stack:
    """Stack implementation using list"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def to_list(self):
        return self.items.copy()

class Queue:
    """Queue implementation using list"""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def to_list(self):
        return self.items.copy()

class PriorityQueue:
    """Priority Queue implementation (higher priority value = higher priority)"""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item, priority):
        self.items.append((priority, item))
        self.items.sort(key=lambda x: x[0], reverse=True)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)[1]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def to_list(self):
        return [item for _, item in self.items]

# ===================== SORTING ALGORITHMS =====================

class SortAlgorithms:
    """Custom sorting algorithms"""
    
    @staticmethod
    def bubble_sort(arr, key=None, reverse=False):
        """Bubble sort implementation"""
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if key:
                    val1, val2 = key(arr[j]), key(arr[j+1])
                else:
                    val1, val2 = arr[j], arr[j+1]
                
                if (val1 > val2) if not reverse else (val1 < val2):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
    
    @staticmethod
    def insertion_sort(arr, key=None, reverse=False):
        """Insertion sort implementation"""
        arr = arr.copy()
        for i in range(1, len(arr)):
            key_item = arr[i]
            j = i - 1
            
            if key:
                key_val = key(key_item)
                while j >= 0:
                    if (key(arr[j]) > key_val) if not reverse else (key(arr[j]) < key_val):
                        arr[j + 1] = arr[j]
                        j -= 1
                    else:
                        break
            else:
                while j >= 0 and ((arr[j] > key_item) if not reverse else (arr[j] < key_item)):
                    arr[j + 1] = arr[j]
                    j -= 1
            
            arr[j + 1] = key_item
        return arr
    
    @staticmethod
    def selection_sort(arr, key=None, reverse=False):
        """Selection sort implementation"""
        arr = arr.copy()
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if key:
                    val1, val2 = key(arr[min_idx]), key(arr[j])
                else:
                    val1, val2 = arr[min_idx], arr[j]
                
                if (val1 > val2) if not reverse else (val1 < val2):
                    min_idx = j
            
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    @staticmethod
    def quick_sort(arr, key=None, reverse=False):
        """Quick sort implementation"""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        pivot_val = key(pivot) if key else pivot
        
        left = [x for x in arr if ((key(x) if key else x) < pivot_val)]
        middle = [x for x in arr if ((key(x) if key else x) == pivot_val)]
        right = [x for x in arr if ((key(x) if key else x) > pivot_val)]
        
        if reverse:
            return SortAlgorithms.quick_sort(right, key, reverse) + middle + SortAlgorithms.quick_sort(left, key, reverse)
        return SortAlgorithms.quick_sort(left, key, reverse) + middle + SortAlgorithms.quick_sort(right, key, reverse)
    
    @staticmethod
    def merge_sort(arr, key=None, reverse=False):
        """Merge sort implementation"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortAlgorithms.merge_sort(arr[:mid], key, reverse)
        right = SortAlgorithms.merge_sort(arr[mid:], key, reverse)
        
        return SortAlgorithms._merge(left, right, key, reverse)
    
    @staticmethod
    def _merge(left, right, key, reverse):
        """Merge helper for merge sort"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            left_val = key(left[i]) if key else left[i]
            right_val = key(right[j]) if key else right[j]
            
            if (left_val <= right_val) if not reverse else (left_val >= right_val):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result

# ===================== SEARCH ALGORITHMS =====================

class SearchAlgorithms:
    """Custom search algorithms"""
    
    @staticmethod
    def linear_search(arr, target, key=None):
        """Linear search implementation"""
        for i, item in enumerate(arr):
            val = key(item) if key else item
            if val == target:
                return i
        return -1
    
    @staticmethod
    def binary_search(arr, target, key=None):
        """Binary search implementation (requires sorted array)"""
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            mid_val = key(arr[mid]) if key else arr[mid]
            
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
    
    @staticmethod
    def keyword_search(arr, keywords, key=None):
        """Search for items containing any of the keywords"""
        results = []
        keywords_lower = [k.lower() for k in keywords]
        
        for item in arr:
            text = (key(item) if key else str(item)).lower()
            if any(keyword in text for keyword in keywords_lower):
                results.append(item)
        
        return results
    
    @staticmethod
    def quick_select(arr, k, key=None):
        """Quick select algorithm to find kth smallest element"""
        if len(arr) == 1:
            return arr[0]
        
        pivot = arr[len(arr) // 2]
        pivot_val = key(pivot) if key else pivot
        
        left = [x for x in arr if ((key(x) if key else x) < pivot_val)]
        middle = [x for x in arr if ((key(x) if key else x) == pivot_val)]
        right = [x for x in arr if ((key(x) if key else x) > pivot_val)]
        
        if k < len(left):
            return SearchAlgorithms.quick_select(left, k, key)
        elif k < len(left) + len(middle):
            return middle[0]
        else:
            return SearchAlgorithms.quick_select(right, k - len(left) - len(middle), key)

# ===================== DATA MODELS =====================

class User:
    """User data model"""
    def __init__(self, username, name, email, password, bio="", dob="", profile_pic=""):
        self.username = username
        self.name = name
        self.email = email
        self.password = self._hash_password(password)
        self.bio = bio
        self.dob = dob
        self.profile_pic = profile_pic
        self.friends = []  # List of usernames
        self.friend_requests_sent = []
        self.friend_requests_received = []
        self.created_at = datetime.now().isoformat()
    
    def _hash_password(self, password):
        """Hash password for security"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def check_password(self, password):
        """Verify password"""
        return self.password == self._hash_password(password)
    
    def to_dict(self):
        """Convert to dictionary for JSON serialization"""
        return {
            'username': self.username,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'bio': self.bio,
            'dob': self.dob,
            'profile_pic': self.profile_pic,
            'friends': self.friends,
            'friend_requests_sent': self.friend_requests_sent,
            'friend_requests_received': self.friend_requests_received,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        """Create User from dictionary"""
        user = User.__new__(User)
        user.username = data['username']
        user.name = data['name']
        user.email = data['email']
        user.password = data['password']
        user.bio = data.get('bio', '')
        user.dob = data.get('dob', '')
        user.profile_pic = data.get('profile_pic', '')
        user.friends = data.get('friends', [])
        user.friend_requests_sent = data.get('friend_requests_sent', [])
        user.friend_requests_received = data.get('friend_requests_received', [])
        user.created_at = data.get('created_at', datetime.now().isoformat())
        return user

class Comment:
    """Comment data model"""
    def __init__(self, username, text, timestamp=None):
        self.username = username
        self.text = text
        self.timestamp = timestamp or datetime.now().isoformat()
    
    def to_dict(self):
        return {
            'username': self.username,
            'text': self.text,
            'timestamp': self.timestamp
        }
    
    @staticmethod
    def from_dict(data):
        return Comment(data['username'], data['text'], data['timestamp'])

class Post:
    """Post data model"""
    def __init__(self, username, text, media_path="", timestamp=None):
        self.username = username
        self.text = text
        self.media_path = media_path
        self.likes = []  # List of usernames
        self.views = []  # List of usernames
        self.comments = Stack()  # Stack of Comment objects
        self.timestamp = timestamp or datetime.now().isoformat()
        self.post_id = self._generate_id()
    
    def _generate_id(self):
        """Generate unique post ID"""
        return hashlib.md5(f"{self.username}{self.timestamp}".encode()).hexdigest()
    
    def add_like(self, username):
        """Add like from user"""
        if username not in self.likes:
            self.likes.append(username)
            return True
        return False
    
    def remove_like(self, username):
        """Remove like from user"""
        if username in self.likes:
            self.likes.remove(username)
            return True
        return False
    
    def add_view(self, username):
        """Add view from user (max 1 per user)"""
        if username not in self.views:
            self.views.append(username)
            return True
        return False
    
    def remove_view(self, username):
        """Remove view from user"""
        if username in self.views:
            self.views.remove(username)
            return True
        return False
    
    def add_comment(self, comment):
        """Add comment (stack - most recent on top)"""
        self.comments.push(comment)
    
    def get_comments(self):
        """Get all comments as list (most recent first)"""
        return self.comments.to_list()[::-1]
    
    def to_dict(self):
        return {
            'post_id': self.post_id,
            'username': self.username,
            'text': self.text,
            'media_path': self.media_path,
            'likes': self.likes,
            'views': self.views,
            'comments': [c.to_dict() for c in self.comments.to_list()],
            'timestamp': self.timestamp
        }
    
    @staticmethod
    def from_dict(data):
        post = Post(
            data['username'],
            data['text'],
            data.get('media_path', ''),
            data['timestamp']
        )
        post.post_id = data['post_id']
        post.likes = data.get('likes', [])
        post.views = data.get('views', [])
        
        # Rebuild comment stack
        for comment_data in data.get('comments', []):
            post.comments.push(Comment.from_dict(comment_data))
        
        return post

class Notification:
    """Notification data model"""
    TYPE_LIKE = "like"
    TYPE_COMMENT = "comment"
    TYPE_FRIEND_REQUEST = "friend_request"
    TYPE_FRIEND_ACCEPTED = "friend_accepted"
    
    def __init__(self, notif_type, from_user, message, timestamp=None):
        self.type = notif_type
        self.from_user = from_user
        self.message = message
        self.timestamp = timestamp or datetime.now().isoformat()
        self.read = False
    
    def to_dict(self):
        return {
            'type': self.type,
            'from_user': self.from_user,
            'message': self.message,
            'timestamp': self.timestamp,
            'read': self.read
        }
    
    @staticmethod
    def from_dict(data):
        notif = Notification(
            data['type'],
            data['from_user'],
            data['message'],
            data['timestamp']
        )
        notif.read = data.get('read', False)
        return notif

# ===================== DATA MANAGER =====================

class DataManager:
    """Handles all data persistence and management"""
    
    DATA_DIR = "social_media_data"
    USERS_FILE = "users.txt"
    POSTS_FILE = "posts.txt"
    NOTIFICATIONS_FILE = "notifications.txt"
    
    def __init__(self):
        self.users = LinkedList()  # Linked list of users
        self.posts = Queue()  # Queue of posts
        self.notifications = {}  # Dict of username -> Queue of notifications
        self.undo_stack = Stack()  # Stack for undo operations
        
        self._ensure_data_dir()
        self.load_all_data()
    
    def _ensure_data_dir(self):
        """Create data directory if it doesn't exist"""
        if not os.path.exists(self.DATA_DIR):
            os.makedirs(self.DATA_DIR)
    
    def _get_file_path(self, filename):
        """Get full file path"""
        return os.path.join(self.DATA_DIR, filename)
    
    @staticmethod
    def validate_email(email):
        """Validate email format"""
        if '@' not in email:
            return False, "Email must contain '@' symbol"
        
        parts = email.split('@')
        if len(parts) != 2:
            return False, "Invalid email format"
        
        if not parts[0] or not parts[1]:
            return False, "Invalid email format"
        
        if '.' not in parts[1]:
            return False, "Email domain must contain a '.'"
        
        return True, "Valid email"
    
    @staticmethod
    def validate_date(date_str):
        """Validate date format (DD/MM/YYYY or DD-MM-YYYY)"""
        if not date_str.strip():
            return True, "Date is optional"  # Empty is OK
        
        # Check for valid separators
        if '/' in date_str:
            separator = '/'
        elif '-' in date_str:
            separator = '-'
        else:
            return False, "Date must be in DD/MM/YYYY or DD-MM-YYYY format"
        
        parts = date_str.split(separator)
        
        if len(parts) != 3:
            return False, "Date must be in DD/MM/YYYY or DD-MM-YYYY format"
        
        day, month, year = parts
        
        # Check if all parts are numeric
        if not (day.isdigit() and month.isdigit() and year.isdigit()):
            return False, "Date must contain only numbers (DD/MM/YYYY or DD-MM-YYYY)"
        
        # Convert to integers
        try:
            day_int = int(day)
            month_int = int(month)
            year_int = int(year)
        except ValueError:
            return False, "Invalid date values"
        
        # Validate ranges
        if not (1 <= day_int <= 31):
            return False, "Day must be between 1 and 31"
        
        if not (1 <= month_int <= 12):
            return False, "Month must be between 1 and 12"
        
        if not (1900 <= year_int <= 2025):
            return False, "Year must be between 1900 and 2025"
        
        # Check days in month
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if day_int > days_in_month[month_int - 1]:
            return False, f"Invalid day for month {month_int}"
        
        return True, "Valid date"
    
    @staticmethod
    def validate_name(name):
        """Validate name - no digits or special symbols allowed"""
        if not name.strip():
            return False, "Name cannot be empty"
        
        # Check for digits
        if any(char.isdigit() for char in name):
            return False, "Name cannot contain numbers"
        
        # Check for special symbols (allow spaces, hyphens, apostrophes)
        allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'")
        if not all(char in allowed_chars for char in name):
            return False, "Name can only contain letters, spaces, hyphens, and apostrophes"
        
        return True, "Valid name"
    
    # ========== USER OPERATIONS ==========
    
    def create_user(self, username, name, email, password, bio="", dob=""):
        """Create new user"""
        # Validate name
        name_valid, name_msg = self.validate_name(name)
        if not name_valid:
            return None, name_msg
        
        # Validate email
        email_valid, email_msg = self.validate_email(email)
        if not email_valid:
            return None, email_msg
        
        # Validate date of birth
        dob_valid, dob_msg = self.validate_date(dob)
        if not dob_valid:
            return None, dob_msg
        
        # Check if username exists
        if self.get_user(username):
            return None, "Username already exists"
        
        # Check if email exists
        if self.users.find(lambda u: u.email == email):
            return None, "Email already exists"
        
        user = User(username, name, email, password, bio, dob)
        self.users.append(user)
        self.notifications[username] = Queue()
        self.save_users()
        return user, "User created successfully"
    
    def get_user(self, username):
        """Get user by username"""
        return self.users.find(lambda u: u.username == username)
    
    def update_user(self, username, **kwargs):
        """Update user details"""
        user = self.get_user(username)
        if not user:
            return False
        
        for key, value in kwargs.items():
            if hasattr(user, key):
                setattr(user, key, value)
        
        self.save_users()
        return True
    
    def authenticate_user(self, username, password):
        """Authenticate user"""
        user = self.get_user(username)
        if user and user.check_password(password):
            return user
        return None
    
    def search_users(self, query):
        """Search users by username or name"""
        query_lower = query.lower()
        results = []
        current = self.users.head
        while current:
            user = current.data
            if (query_lower in user.username.lower() or 
                query_lower in user.name.lower()):
                results.append(user)
            current = current.next
        return results
    
    # ========== FRIENDSHIP OPERATIONS ==========
    
    def send_friend_request(self, from_username, to_username):
        """Send friend request"""
        from_user = self.get_user(from_username)
        to_user = self.get_user(to_username)
        
        if not from_user or not to_user:
            return False, "User not found"
        
        if to_username in from_user.friends:
            return False, "Already friends"
        
        if to_username in from_user.friend_requests_sent:
            return False, "Request already sent"
        
        from_user.friend_requests_sent.append(to_username)
        to_user.friend_requests_received.append(from_username)
        
        # Create notification
        notif = Notification(
            Notification.TYPE_FRIEND_REQUEST,
            from_username,
            f"{from_user.name} sent you a friend request"
        )
        self.add_notification(to_username, notif)
        
        self.save_users()
        self.save_notifications()
        return True, "Friend request sent"
    
    def accept_friend_request(self, username, from_username):
        """Accept friend request"""
        user = self.get_user(username)
        from_user = self.get_user(from_username)
        
        if not user or not from_user:
            return False
        
        if from_username not in user.friend_requests_received:
            return False
        
        # Add to friends lists
        user.friends.append(from_username)
        from_user.friends.append(username)
        
        # Remove from requests
        user.friend_requests_received.remove(from_username)
        from_user.friend_requests_sent.remove(username)
        
        # Create notification
        notif = Notification(
            Notification.TYPE_FRIEND_ACCEPTED,
            username,
            f"{user.name} accepted your friend request"
        )
        self.add_notification(from_username, notif)
        
        self.save_users()
        self.save_notifications()
        return True
    
    def get_friends(self, username):
        """Get user's friends"""
        user = self.get_user(username)
        if not user:
            return []
        
        friends = []
        for friend_username in user.friends:
            friend = self.get_user(friend_username)
            if friend:
                friends.append(friend)
        return friends
    
    # ========== POST OPERATIONS ==========
    
    def create_post(self, username, text, media_path=""):
        """Create new post"""
        if not text.strip():
            return None, "Text content is required"
        
        post = Post(username, text, media_path)
        self.posts.enqueue(post)
        self.save_posts()
        return post, "Post created successfully"
    
    def delete_post(self, post_id, username):
        """Delete post"""
        posts_list = self.posts.to_list()
        post_to_delete = None
        
        for post in posts_list:
            if post.post_id == post_id and post.username == username:
                post_to_delete = post
                break
        
        if post_to_delete:
            posts_list.remove(post_to_delete)
            self.posts = Queue()
            for p in posts_list:
                self.posts.enqueue(p)
            
            # Add to undo stack
            self.undo_stack.push(('delete_post', post_to_delete))
            
            self.save_posts()
            return True
        return False
    
    def edit_post(self, post_id, username, new_text, new_media_path=None):
        """Edit post content"""
        posts_list = self.posts.to_list()
        
        for post in posts_list:
            if post.post_id == post_id and post.username == username:
                # Store old content for potential undo
                old_text = post.text
                old_media = post.media_path
                
                # Update post
                post.text = new_text
                if new_media_path is not None:
                    post.media_path = new_media_path
                
                self.save_posts()
                return True, "Post updated successfully"
        
        return False, "Post not found or unauthorized"
    
    def like_post(self, post_id, username):
        """Like a post"""
        posts_list = self.posts.to_list()
        for post in posts_list:
            if post.post_id == post_id:
                if post.add_like(username):
                    # Add to undo stack
                    self.undo_stack.push(('like', post_id, username))
                    
                    # Create notification
                    if post.username != username:
                        liker = self.get_user(username)
                        notif = Notification(
                            Notification.TYPE_LIKE,
                            username,
                            f"{liker.name} liked your post"
                        )
                        self.add_notification(post.username, notif)
                        self.save_notifications()
                    
                    self.save_posts()
                    return True
        return False
    
    def view_post(self, post_id, username):
        """View a post (max 1 per user)"""
        posts_list = self.posts.to_list()
        for post in posts_list:
            if post.post_id == post_id:
                if post.add_view(username):
                    # Add to undo stack
                    self.undo_stack.push(('view', post_id, username))
                    self.save_posts()
                    return True
        return False
    
    def comment_on_post(self, post_id, username, text):
        """Comment on a post"""
        posts_list = self.posts.to_list()
        for post in posts_list:
            if post.post_id == post_id:
                comment = Comment(username, text)
                post.add_comment(comment)
                
                # Create notification
                if post.username != username:
                    commenter = self.get_user(username)
                    notif = Notification(
                        Notification.TYPE_COMMENT,
                        username,
                        f"{commenter.name} commented on your post"
                    )
                    self.add_notification(post.username, notif)
                    self.save_notifications()
                
                self.save_posts()
                return True
        return False
    
    def get_all_posts(self):
        """Get all posts"""
        return self.posts.to_list()
    
    def get_user_posts(self, username):
        """Get posts by specific user"""
        all_posts = self.posts.to_list()
        return [p for p in all_posts if p.username == username]
    
    def get_friends_posts(self, username):
        """Get posts from user's friends"""
        user = self.get_user(username)
        if not user:
            return []
        
        all_posts = self.posts.to_list()
        friends_posts = [p for p in all_posts if p.username in user.friends or p.username == username]
        return friends_posts
    
    def search_posts(self, query, posts_list=None):
        """Search posts by text content"""
        if posts_list is None:
            posts_list = self.get_all_posts()
        
        keywords = query.lower().split()
        return SearchAlgorithms.keyword_search(
            posts_list,
            keywords,
            key=lambda p: p.text
        )
    
    # ========== NOTIFICATION OPERATIONS ==========
    
    def add_notification(self, username, notification):
        """Add notification for user"""
        if username not in self.notifications:
            self.notifications[username] = Queue()
        self.notifications[username].enqueue(notification)
    
    def get_notifications(self, username):
        """Get all notifications for user"""
        if username not in self.notifications:
            return []
        return self.notifications[username].to_list()
    
    def mark_notifications_read(self, username):
        """Mark all notifications as read"""
        if username in self.notifications:
            for notif in self.notifications[username].to_list():
                notif.read = True
            self.save_notifications()
    
    # ========== UNDO OPERATIONS ==========
    
    def undo_last_action(self):
        """Undo the last action"""
        if self.undo_stack.is_empty():
            return False, "No actions to undo"
        
        action = self.undo_stack.pop()
        
        if action[0] == 'like':
            _, post_id, username = action
            posts_list = self.posts.to_list()
            for post in posts_list:
                if post.post_id == post_id:
                    post.remove_like(username)
                    self.save_posts()
                    return True, "Like undone"
        
        elif action[0] == 'delete_post':
            _, post = action
            self.posts.enqueue(post)
            self.save_posts()
            return True, "Post deletion undone"
        
        return False, "Failed to undo action"
    
    # ========== FILE OPERATIONS ==========
    
    def save_users(self):
        """Save users to file"""
        users_data = [u.to_dict() for u in self.users.to_list()]
        with open(self._get_file_path(self.USERS_FILE), 'w') as f:
            json.dump(users_data, f, indent=2)
    
    def load_users(self):
        """Load users from file"""
        filepath = self._get_file_path(self.USERS_FILE)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                users_data = json.load(f)
                for user_data in users_data:
                    user = User.from_dict(user_data)
                    self.users.append(user)
                    if user.username not in self.notifications:
                        self.notifications[user.username] = Queue()
    
    def save_posts(self):
        """Save posts to file"""
        posts_data = [p.to_dict() for p in self.posts.to_list()]
        with open(self._get_file_path(self.POSTS_FILE), 'w') as f:
            json.dump(posts_data, f, indent=2)
    
    def load_posts(self):
        """Load posts from file"""
        filepath = self._get_file_path(self.POSTS_FILE)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                posts_data = json.load(f)
                for post_data in posts_data:
                    post = Post.from_dict(post_data)
                    self.posts.enqueue(post)
    
    def save_notifications(self):
        """Save notifications to file"""
        notif_data = {}
        for username, notif_queue in self.notifications.items():
            notif_data[username] = [n.to_dict() for n in notif_queue.to_list()]
        
        with open(self._get_file_path(self.NOTIFICATIONS_FILE), 'w') as f:
            json.dump(notif_data, f, indent=2)
    
    def load_notifications(self):
        """Load notifications from file"""
        filepath = self._get_file_path(self.NOTIFICATIONS_FILE)
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                notif_data = json.load(f)
                for username, notifs in notif_data.items():
                    self.notifications[username] = Queue()
                    for notif_dict in notifs:
                        notif = Notification.from_dict(notif_dict)
                        self.notifications[username].enqueue(notif)
    
    def load_all_data(self):
        """Load all data from files"""
        self.load_users()
        self.load_posts()
        self.load_notifications()

# ===================== UI COMPONENTS =====================

class PostCard(ctk.CTkFrame):
    """Individual post card widget"""
    def __init__(self, parent, post, current_user, data_manager, on_update=None):
        super().__init__(parent, fg_color=Theme.CARD_BG, corner_radius=Theme.CORNER_RADIUS)
        
        self.post = post
        self.current_user = current_user
        self.data_manager = data_manager
        self.on_update = on_update
        self.comments_expanded = False
        self.view_registered = False
        
        self.setup_ui()
        
        # Register view automatically when card is visible (after 0.5 seconds)
        self.after(500, self.auto_register_view)
    
    def auto_register_view(self):
        """Automatically register view when post is visible"""
        if not self.view_registered and self.winfo_viewable():
            if self.data_manager.view_post(self.post.post_id, self.current_user):
                self.view_registered = True
                self.refresh_ui()
    
    def setup_ui(self):
        """Setup post card UI"""
        self.grid_columnconfigure(0, weight=1)
        
        # Header with user info
        header_frame = ctk.CTkFrame(self, fg_color="transparent")
        header_frame.grid(row=0, column=0, sticky="ew", padx=Theme.PADDING, pady=(Theme.PADDING, 5))
        
        # Profile picture placeholder
        profile_label = ctk.CTkLabel(
            header_frame,
            text="👤",
            font=("Segoe UI", 24),
            width=40,
            height=40
        )
        profile_label.pack(side="left", padx=(0, 10))
        
        # User info
        user = self.data_manager.get_user(self.post.username)
        user_info_frame = ctk.CTkFrame(header_frame, fg_color="transparent")
        user_info_frame.pack(side="left", fill="both", expand=True)
        
        name_label = ctk.CTkLabel(
            user_info_frame,
            text=user.name if user else self.post.username,
            font=Theme.FONT_SUBHEADING,
            anchor="w"
        )
        name_label.pack(anchor="w")
        
        username_label = ctk.CTkLabel(
            user_info_frame,
            text=f"@{self.post.username}",
            font=Theme.FONT_SMALL,
            text_color=Theme.TEXT_SECONDARY,
            anchor="w"
        )
        username_label.pack(anchor="w")
        
        # Timestamp
        time_str = datetime.fromisoformat(self.post.timestamp).strftime("%b %d, %Y %I:%M %p")
        time_label = ctk.CTkLabel(
            header_frame,
            text=time_str,
            font=Theme.FONT_SMALL,
            text_color=Theme.TEXT_SECONDARY
        )
        time_label.pack(side="right")
        
        # Post text content
        text_label = ctk.CTkLabel(
            self,
            text=self.post.text,
            font=Theme.FONT_BODY,
            wraplength=500,
            anchor="w",
            justify="left"
        )
        text_label.grid(row=1, column=0, sticky="ew", padx=Theme.PADDING, pady=5)
        
        # Media placeholder (if exists)
        if self.post.media_path:
            try:
                # Try to load and display the actual media
                img = Image.open(self.post.media_path)
                # Resize to fit width while maintaining aspect ratio
                max_width = 500
                ratio = max_width / img.width
                new_height = int(img.height * ratio)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
                
                photo = ctk.CTkImage(light_image=img, dark_image=img, size=(max_width, new_height))
                
                media_label = ctk.CTkLabel(
                    self,
                    image=photo,
                    text=""
                )
                media_label.image = photo  # Keep a reference
                media_label.grid(row=2, column=0, sticky="ew", padx=Theme.PADDING, pady=5)
            except Exception as e:
                # Fallback if image can't be loaded
                media_label = ctk.CTkLabel(
                    self,
                    text=f"📷 {os.path.basename(self.post.media_path)}",
                    font=Theme.FONT_SMALL,
                    text_color=Theme.PRIMARY,
                    anchor="w"
                )
                media_label.grid(row=2, column=0, sticky="ew", padx=Theme.PADDING, pady=5)
        
        # Actions frame
        actions_frame = ctk.CTkFrame(self, fg_color="transparent")
        actions_frame.grid(row=3, column=0, sticky="ew", padx=Theme.PADDING, pady=5)
        
        # Like button
        liked = self.current_user in self.post.likes
        self.like_btn = ctk.CTkButton(
            actions_frame,
            text=f"{'❤️' if liked else '🤍'} {len(self.post.likes)}",
            width=80,
            height=30,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY if liked else Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=self.toggle_like
        )
        self.like_btn.pack(side="left", padx=5)
        
        # View count (no button, just display)
        viewed = self.current_user in self.post.views
        self.view_label = ctk.CTkLabel(
            actions_frame,
            text=f"👁️ {len(self.post.views)}",
            font=Theme.FONT_BODY,
            text_color=Theme.PRIMARY if viewed else Theme.TEXT_SECONDARY
        )
        self.view_label.pack(side="left", padx=10)
        
        # Comment button
        self.comment_btn = ctk.CTkButton(
            actions_frame,
            text=f"💬 {len(self.post.get_comments())}",
            width=80,
            height=30,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=self.toggle_comments
        )
        self.comment_btn.pack(side="left", padx=5)
        
        # Delete button (only for own posts)
        if self.post.username == self.current_user:
            edit_btn = ctk.CTkButton(
                actions_frame,
                text="✏️",
                width=40,
                height=30,
                corner_radius=Theme.BUTTON_CORNER_RADIUS,
                fg_color=Theme.SECONDARY,
                hover_color=Theme.BUTTON_HOVER,
                command=self.edit_post
            )
            edit_btn.pack(side="right", padx=5)
            
            delete_btn = ctk.CTkButton(
                actions_frame,
                text="🗑️",
                width=40,
                height=30,
                corner_radius=Theme.BUTTON_CORNER_RADIUS,
                fg_color="#C13584",
                hover_color="#E1306C",
                command=self.delete_post
            )
            delete_btn.pack(side="right", padx=5)
        
        # Comment input
        comment_frame = ctk.CTkFrame(self, fg_color="transparent")
        comment_frame.grid(row=4, column=0, sticky="ew", padx=Theme.PADDING, pady=5)
        comment_frame.grid_columnconfigure(0, weight=1)
        
        self.comment_entry = ctk.CTkEntry(
            comment_frame,
            placeholder_text="Write a comment...",
            height=35,
            corner_radius=Theme.BUTTON_CORNER_RADIUS
        )
        self.comment_entry.grid(row=0, column=0, sticky="ew", padx=(0, 5))
        
        send_btn = ctk.CTkButton(
            comment_frame,
            text="Send",
            width=60,
            height=35,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=self.add_comment
        )
        send_btn.grid(row=0, column=1)
        
        # Comments preview (2-3 recent)
        self.comments_preview_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.comments_preview_frame.grid(row=5, column=0, sticky="ew", padx=Theme.PADDING, pady=5)
        
        # Comments expanded section
        self.comments_expanded_frame = ctk.CTkFrame(self, fg_color="transparent")
        
        self.refresh_comments()
    
    def toggle_like(self):
        """Toggle like on post"""
        if self.current_user in self.post.likes:
            self.post.remove_like(self.current_user)
            self.data_manager.save_posts()
        else:
            self.data_manager.like_post(self.post.post_id, self.current_user)
        
        self.refresh_ui()
    
    def add_comment(self):
        """Add comment to post"""
        text = self.comment_entry.get().strip()
        if text:
            self.data_manager.comment_on_post(self.post.post_id, self.current_user, text)
            self.comment_entry.delete(0, 'end')
            # Update comment count button
            self.comment_btn.configure(text=f"💬 {len(self.post.get_comments())}")
            self.refresh_comments()
    
    def delete_post(self):
        """Delete this post"""
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this post?"):
            self.data_manager.delete_post(self.post.post_id, self.current_user)
            if self.on_update:
                self.on_update()
    
    def edit_post(self):
        """Edit this post"""
        dialog = ctk.CTkToplevel(self.master)
        dialog.title("Edit Post")
        dialog.geometry("500x400")
        dialog.transient(self.master)
        dialog.grab_set()
        
        ctk.CTkLabel(dialog, text="Edit Post", font=Theme.FONT_HEADING).pack(pady=20)
        
        # Text input
        ctk.CTkLabel(dialog, text="Post Content *", font=Theme.FONT_BODY, anchor="w").pack(anchor="w", padx=30)
        text_input = ctk.CTkTextbox(
            dialog,
            height=150,
            corner_radius=Theme.BUTTON_CORNER_RADIUS
        )
        text_input.pack(padx=30, pady=10, fill="both", expand=True)
        text_input.insert("1.0", self.post.text)
        
        # Media info
        media_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        media_frame.pack(fill="x", padx=30, pady=10)
        
        current_media = os.path.basename(self.post.media_path) if self.post.media_path else "No media"
        media_label = ctk.CTkLabel(media_frame, text=f"Current: {current_media}", font=Theme.FONT_SMALL, text_color=Theme.TEXT_SECONDARY)
        media_label.pack(side="left")
        
        new_media_path = [self.post.media_path]  # Use list to allow modification in nested function
        
        def select_media():
            filepath = filedialog.askopenfilename(
                title="Select Media",
                filetypes=[("Image/Video", "*.jpg *.jpeg *.png *.gif *.mp4 *.avi")]
            )
            if filepath:
                new_media_path[0] = filepath
                media_label.configure(text=f"New: {os.path.basename(filepath)}")
        
        media_btn = ctk.CTkButton(
            media_frame,
            text="Change Media",
            width=120,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=select_media
        )
        media_btn.pack(side="right")
        
        # Buttons
        def save_changes():
            text = text_input.get("1.0", "end-1c").strip()
            if not text:
                messagebox.showerror("Error", "Post content is required!")
                return
            
            success, message = self.data_manager.edit_post(
                self.post.post_id,
                self.current_user,
                text,
                new_media_path[0]
            )
            
            if success:
                messagebox.showinfo("Success", message)
                dialog.destroy()
                if self.on_update:
                    self.on_update()
            else:
                messagebox.showerror("Error", message)
        
        save_btn = ctk.CTkButton(
            dialog,
            text="Save Changes",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=save_changes
        )
        save_btn.pack(pady=10)
        
        cancel_btn = ctk.CTkButton(
            dialog,
            text="Cancel",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=dialog.destroy
        )
        cancel_btn.pack()
    
    def toggle_comments(self):
        """Toggle expanded comments view"""
        self.comments_expanded = not self.comments_expanded
        
        if self.comments_expanded:
            self.comments_preview_frame.grid_remove()
            self.comments_expanded_frame.grid(row=5, column=0, sticky="ew", padx=Theme.PADDING, pady=5)
        else:
            self.comments_expanded_frame.grid_remove()
            self.comments_preview_frame.grid(row=5, column=0, sticky="ew", padx=Theme.PADDING, pady=5)
        
        self.refresh_comments()
    
    def refresh_comments(self):
        """Refresh comments display"""
        # Clear existing comments
        for widget in self.comments_preview_frame.winfo_children():
            widget.destroy()
        for widget in self.comments_expanded_frame.winfo_children():
            widget.destroy()
        
        comments = self.post.get_comments()
        
        if not comments:
            return
        
        # Show preview (2-3 recent comments)
        preview_count = min(3, len(comments))
        for i in range(preview_count):
            self.create_comment_widget(comments[i], self.comments_preview_frame)
        
        if len(comments) > preview_count:
            show_all_btn = ctk.CTkButton(
                self.comments_preview_frame,
                text=f"Show all {len(comments)} comments",
                height=25,
                corner_radius=Theme.BUTTON_CORNER_RADIUS,
                fg_color=Theme.BACKGROUND_LIGHT,
                hover_color=Theme.BUTTON_HOVER,
                command=self.toggle_comments
            )
            show_all_btn.pack(anchor="w", pady=5)
        
        # Show all comments in expanded view
        for comment in comments:
            self.create_comment_widget(comment, self.comments_expanded_frame)
    
    def create_comment_widget(self, comment, parent):
        """Create a comment widget"""
        comment_frame = ctk.CTkFrame(parent, fg_color=Theme.BACKGROUND_LIGHT, corner_radius=10)
        comment_frame.pack(fill="x", pady=2)
        
        user = self.data_manager.get_user(comment.username)
        username_label = ctk.CTkLabel(
            comment_frame,
            text=f"@{comment.username}",
            font=Theme.FONT_SMALL,
            text_color=Theme.PRIMARY,
            anchor="w"
        )
        username_label.pack(anchor="w", padx=10, pady=(5, 0))
        
        text_label = ctk.CTkLabel(
            comment_frame,
            text=comment.text,
            font=Theme.FONT_SMALL,
            anchor="w",
            wraplength=450
        )
        text_label.pack(anchor="w", padx=10, pady=(0, 5))
    
    def refresh_ui(self):
        """Refresh UI elements"""
        liked = self.current_user in self.post.likes
        self.like_btn.configure(
            text=f"{'❤️' if liked else '🤍'} {len(self.post.likes)}",
            fg_color=Theme.PRIMARY if liked else Theme.BACKGROUND_LIGHT
        )
        
        viewed = self.current_user in self.post.views
        self.view_label.configure(
            text=f"👁️ {len(self.post.views)}",
            text_color=Theme.PRIMARY if viewed else Theme.TEXT_SECONDARY
        )

# ===================== MAIN APPLICATION =====================

class SocialMediaApp(ctk.CTk):
    """Main application window"""
    def __init__(self):
        super().__init__()
        
        self.title("Ministagram")
        self.geometry("1200x800")
        
        # Set theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.data_manager = DataManager()
        self.current_user = None
        
        self.show_splash_screen()
    
    def show_splash_screen(self):
        """Show Instagram-style loading splash screen"""
        # Create splash frame
        splash_frame = ctk.CTkFrame(self, fg_color=Theme.BACKGROUND_DARK)
        splash_frame.place(relx=0, rely=0, relwidth=1, relheight=1)
        
        # Gradient background simulation with multiple frames
        gradient_top = ctk.CTkFrame(
            splash_frame, 
            fg_color=Theme.GRADIENT_START,
            height=266
        )
        gradient_top.place(relx=0, rely=0, relwidth=1, relheight=0.33)
        
        gradient_mid = ctk.CTkFrame(
            splash_frame,
            fg_color=Theme.GRADIENT_MID,
            height=267
        )
        gradient_mid.place(relx=0, rely=0.33, relwidth=1, relheight=0.34)
        
        gradient_bottom = ctk.CTkFrame(
            splash_frame,
            fg_color=Theme.GRADIENT_END,
            height=267
        )
        gradient_bottom.place(relx=0, rely=0.67, relwidth=1, relheight=0.33)
        
        # Center container
        center_container = ctk.CTkFrame(splash_frame, fg_color="transparent")
        center_container.place(relx=0.5, rely=0.5, anchor="center")
        
        # Instagram-style logo
        logo_frame = ctk.CTkFrame(
            center_container,
            fg_color="white",
            corner_radius=25,
            width=120,
            height=120
        )
        logo_frame.pack(pady=20)
        logo_frame.pack_propagate(False)
        
        # Camera icon simulation using emoji
        camera_icon = ctk.CTkLabel(
            logo_frame,
            text="📸",
            font=("Segoe UI", 60),
            text_color=Theme.PRIMARY
        )
        camera_icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # App name
        app_name = ctk.CTkLabel(
            center_container,
            text="Ministagram",
            font=Theme.FONT_LOGO,
            text_color="white"
        )
        app_name.pack(pady=10)
        
        # Loading text
        loading_label = ctk.CTkLabel(
            center_container,
            text="Loading...",
            font=Theme.FONT_BODY,
            text_color="white"
        )
        loading_label.pack(pady=10)
        
        # Animate loading dots
        self.loading_dots = 0
        self.animate_loading(loading_label, splash_frame)
    
    def animate_loading(self, label, splash_frame, count=0):
        """Animate loading dots"""
        if count < 25:  # Show loading for ~1.5 seconds 
            dots = "." * (count % 4)
            label.configure(text=f"Loading{dots}")
            self.after(100, lambda: self.animate_loading(label, splash_frame, count + 1))
        else:
            # Destroy splash and show login
            splash_frame.destroy()
            self.show_login_screen()
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        """Show login/signup screen"""
        self.clear_window()
        
        # Gradient background
        gradient_top = ctk.CTkFrame(self, fg_color=Theme.GRADIENT_START, height=266)
        gradient_top.place(relx=0, rely=0, relwidth=1, relheight=0.33)
        
        gradient_mid = ctk.CTkFrame(self, fg_color=Theme.GRADIENT_MID, height=267)
        gradient_mid.place(relx=0, rely=0.33, relwidth=1, relheight=0.34)
        
        gradient_bottom = ctk.CTkFrame(self, fg_color=Theme.GRADIENT_END, height=267)
        gradient_bottom.place(relx=0, rely=0.67, relwidth=1, relheight=0.33)
        
        # Center frame
        center_frame = ctk.CTkFrame(self, fg_color="transparent")
        center_frame.place(relx=0.5, rely=0.5, anchor="center")
        
        # Logo
        logo_frame = ctk.CTkFrame(center_frame, fg_color="white", corner_radius=20, width=100, height=100)
        logo_frame.pack(pady=20)
        logo_frame.pack_propagate(False)
        
        camera_icon = ctk.CTkLabel(logo_frame, text="📸", font=("Segoe UI", 50), text_color=Theme.PRIMARY)
        camera_icon.place(relx=0.5, rely=0.5, anchor="center")
        
        # Title
        title_label = ctk.CTkLabel(
            center_frame,
            text="Ministagram",
            font=Theme.FONT_LOGO,
            text_color="white"
        )
        title_label.pack(pady=10)
        
        # Login form
        login_frame = ctk.CTkFrame(center_frame, fg_color=Theme.CARD_BG, corner_radius=Theme.CORNER_RADIUS)
        login_frame.pack(padx=40, pady=20)
        
        ctk.CTkLabel(login_frame, text="Login", font=Theme.FONT_HEADING).pack(pady=15)
        
        self.login_username = ctk.CTkEntry(
            login_frame,
            placeholder_text="Username",
            width=300,
            height=40,
            corner_radius=Theme.BUTTON_CORNER_RADIUS
        )
        self.login_username.pack(pady=10, padx=30)
        
        self.login_password = ctk.CTkEntry(
            login_frame,
            placeholder_text="Password",
            show="*",
            width=300,
            height=40,
            corner_radius=Theme.BUTTON_CORNER_RADIUS
        )
        self.login_password.pack(pady=10, padx=30)
        
        login_btn = ctk.CTkButton(
            login_frame,
            text="Login",
            width=300,
            height=40,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=self.login
        )
        login_btn.pack(pady=10, padx=30)
        
        signup_btn = ctk.CTkButton(
            login_frame,
            text="Create Account",
            width=300,
            height=40,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=self.show_signup_screen
        )
        signup_btn.pack(pady=(5, 20), padx=30)
    
    def show_signup_screen(self):
        """Show signup screen"""
        self.clear_window()
        
        # Center frame with scrollable
        center_frame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        center_frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.4, relheight=0.8)
        
        # Title
        title_label = ctk.CTkLabel(
            center_frame,
            text="Create Account",
            font=Theme.FONT_TITLE,
            text_color=Theme.PRIMARY
        )
        title_label.pack(pady=20)
        
        # Signup form
        self.signup_name = self.create_entry(center_frame, "Full Name *")
        self.signup_username = self.create_entry(center_frame, "Username *")
        self.signup_email = self.create_entry(center_frame, "Email * (must include @)")
        self.signup_password = self.create_entry(center_frame, "Password *", show="*")
        self.signup_bio = self.create_entry(center_frame, "Bio (optional)")
        
        # Date of birth with format hint
        dob_label = ctk.CTkLabel(
            center_frame,
            text="Date of Birth (DD/MM/YYYY or DD-MM-YYYY)",
            font=Theme.FONT_SMALL,
            text_color=Theme.TEXT_SECONDARY
        )
        dob_label.pack(pady=(10, 0))
        
        self.signup_dob = self.create_entry(center_frame, "DD/MM/YYYY (optional)")
        
        signup_btn = ctk.CTkButton(
            center_frame,
            text="Sign Up",
            width=300,
            height=40,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=self.signup
        )
        signup_btn.pack(pady=15)
        
        back_btn = ctk.CTkButton(
            center_frame,
            text="Back to Login",
            width=300,
            height=40,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=self.show_login_screen
        )
        back_btn.pack(pady=5)
    
    def create_entry(self, parent, placeholder, show=None):
        """Helper to create entry widget"""
        entry = ctk.CTkEntry(
            parent,
            placeholder_text=placeholder,
            width=300,
            height=40,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            show=show
        )
        entry.pack(pady=10)
        return entry
    
    def login(self):
        """Handle login"""
        username = self.login_username.get().strip()
        password = self.login_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Please fill all fields")
            return
        
        user = self.data_manager.authenticate_user(username, password)
        if user:
            self.current_user = username
            self.show_main_screen()
        else:
            messagebox.showerror("Error", "Invalid username or password")
    
    def signup(self):
        """Handle signup"""
        name = self.signup_name.get().strip()
        username = self.signup_username.get().strip()
        email = self.signup_email.get().strip()
        password = self.signup_password.get()
        bio = self.signup_bio.get().strip()
        dob = self.signup_dob.get().strip()
        
        if not all([name, username, email, password]):
            messagebox.showerror("Error", "Please fill required fields")
            return
        
        user, message = self.data_manager.create_user(username, name, email, password, bio, dob)
        if user:
            messagebox.showinfo("Success", "Account created successfully! Welcome!")
            # Automatically log in the user after signup
            self.current_user = username
            self.show_main_screen()
        else:
            messagebox.showerror("Error", message)
    
    def show_main_screen(self):
        """Show main application screen"""
        self.clear_window()
        
        # Configure grid
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        # Left sidebar
        self.create_sidebar()
        
        # Main content area
        self.main_content = ctk.CTkFrame(self, fg_color=Theme.BACKGROUND_DARK)
        self.main_content.grid(row=0, column=1, sticky="nsew")
        
        # Show home feed by default
        self.show_home_feed()
    
    def create_sidebar(self):
        """Create left sidebar with navigation"""
        sidebar = ctk.CTkFrame(self, width=250, fg_color=Theme.CARD_BG, corner_radius=0)
        sidebar.grid(row=0, column=0, sticky="nsew")
        sidebar.grid_propagate(False)
        
        # App logo and title
        logo_container = ctk.CTkFrame(sidebar, fg_color="transparent")
        logo_container.pack(pady=20)
        
        logo_icon = ctk.CTkLabel(logo_container, text="📸", font=("Segoe UI", 30))
        logo_icon.pack()
        
        title_label = ctk.CTkLabel(
            logo_container,
            text="Ministagram",
            font=Theme.FONT_HEADING,
            text_color=Theme.PRIMARY
        )
        title_label.pack()
        
        # Navigation buttons
        self.create_nav_button(sidebar, "🏠 Home", self.show_home_feed)
        self.create_nav_button(sidebar, "👤 Profile", self.show_profile)
        self.create_nav_button(sidebar, "🔔 Notifications", self.show_notifications)
        self.create_nav_button(sidebar, "➕ New Post", self.show_create_post)
        self.create_nav_button(sidebar, "↩️ Undo", self.undo_action)
        
        # Logout button at bottom
        logout_btn = ctk.CTkButton(
            sidebar,
            text="🚪 Logout",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color="#C13584",
            hover_color="#E1306C",
            command=self.logout
        )
        logout_btn.pack(side="bottom", pady=20, padx=20, fill="x")
    
    def create_nav_button(self, parent, text, command):
        """Helper to create navigation button"""
        btn = ctk.CTkButton(
            parent,
            text=text,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color="transparent",
            hover_color=Theme.CARD_BG,
            anchor="w",
            command=command
        )
        btn.pack(pady=5, padx=20, fill="x")
    
    def show_home_feed(self):
        """Show home feed with tabs"""
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # Header
        header = ctk.CTkFrame(self.main_content, fg_color=Theme.CARD_BG, height=100)
        header.pack(fill="x", padx=20, pady=20)
        header.pack_propagate(False)
        
        ctk.CTkLabel(header, text="Feed", font=Theme.FONT_HEADING).pack(side="left", padx=20)
        
        # Search bar
        self.feed_search = ctk.CTkEntry(
            header,
            placeholder_text="Search posts...",
            width=300,
            height=35,
            corner_radius=Theme.BUTTON_CORNER_RADIUS
        )
        self.feed_search.pack(side="right", padx=20)
        self.feed_search.bind('<KeyRelease>', lambda e: self.filter_feed())
        
        # Tab buttons
        tab_frame = ctk.CTkFrame(self.main_content, fg_color="transparent")
        tab_frame.pack(fill="x", padx=20)
        
        self.current_tab = "trending"
        
        self.trending_btn = ctk.CTkButton(
            tab_frame,
            text="🔥 Trending",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.switch_tab("trending")
        )
        self.trending_btn.pack(side="left", padx=5)
        
        self.latest_btn = ctk.CTkButton(
            tab_frame,
            text="🕐 Latest",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.CARD_BG,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.switch_tab("latest")
        )
        self.latest_btn.pack(side="left", padx=5)
        
        self.friends_btn = ctk.CTkButton(
            tab_frame,
            text="👥 Friends",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.CARD_BG,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.switch_tab("friends")
        )
        self.friends_btn.pack(side="left", padx=5)
        
        # Scrollable feed
        self.feed_container = ctk.CTkScrollableFrame(
            self.main_content,
            fg_color="transparent"
        )
        self.feed_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.load_feed()
    
    def switch_tab(self, tab):
        """Switch between feed tabs"""
        self.current_tab = tab
        
        # Update button colors
        self.trending_btn.configure(fg_color=Theme.CARD_BG)
        self.latest_btn.configure(fg_color=Theme.CARD_BG)
        self.friends_btn.configure(fg_color=Theme.CARD_BG)
        
        if tab == "trending":
            self.trending_btn.configure(fg_color=Theme.PRIMARY)
        elif tab == "latest":
            self.latest_btn.configure(fg_color=Theme.PRIMARY)
        else:
            self.friends_btn.configure(fg_color=Theme.PRIMARY)
        
        self.load_feed()
    
    def load_feed(self):
        """Load posts based on current tab"""
        for widget in self.feed_container.winfo_children():
            widget.destroy()
        
        # Get posts based on tab
        if self.current_tab == "friends":
            posts = self.data_manager.get_friends_posts(self.current_user)
        else:
            posts = self.data_manager.get_all_posts()
        
        # Apply search filter if any
        search_query = self.feed_search.get().strip() if hasattr(self, 'feed_search') else ""
        if search_query:
            posts = self.data_manager.search_posts(search_query, posts)
        
        # Sort based on tab
        if self.current_tab == "trending":
            # Sort by likes (trending)
            posts = SortAlgorithms.quick_sort(posts, key=lambda p: len(p.likes), reverse=True)
        elif self.current_tab == "latest":
            # Sort by timestamp (latest)
            posts = SortAlgorithms.merge_sort(posts, key=lambda p: p.timestamp, reverse=True)
        else:
            # Friends - sort by timestamp
            posts = SortAlgorithms.merge_sort(posts, key=lambda p: p.timestamp, reverse=True)
        
        # Display posts
        if not posts:
            no_posts_label = ctk.CTkLabel(
                self.feed_container,
                text="No posts to display",
                font=Theme.FONT_BODY,
                text_color=Theme.TEXT_SECONDARY
            )
            no_posts_label.pack(pady=50)
        else:
            for post in posts:
                card = PostCard(
                    self.feed_container,
                    post,
                    self.current_user,
                    self.data_manager,
                    on_update=self.load_feed
                )
                card.pack(fill="x", pady=10)
    
    def filter_feed(self):
        """Filter feed based on search"""
        self.load_feed()
    
    def show_profile(self):
        """Show user profile"""
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        user = self.data_manager.get_user(self.current_user)
        
        # Profile header
        header = ctk.CTkFrame(self.main_content, fg_color=Theme.CARD_BG, corner_radius=Theme.CORNER_RADIUS)
        header.pack(fill="x", padx=20, pady=20)
        
        profile_content = ctk.CTkFrame(header, fg_color="transparent")
        profile_content.pack(padx=30, pady=30)
        
        # Profile picture
        ctk.CTkLabel(profile_content, text="👤", font=("Segoe UI", 60)).pack()
        
        # User info
        ctk.CTkLabel(profile_content, text=user.name, font=Theme.FONT_HEADING).pack()
        ctk.CTkLabel(profile_content, text=f"@{user.username}", font=Theme.FONT_BODY, text_color=Theme.TEXT_SECONDARY).pack()
        
        if user.bio:
            ctk.CTkLabel(profile_content, text=user.bio, font=Theme.FONT_SMALL, wraplength=400).pack(pady=10)
        
        # Stats
        stats_frame = ctk.CTkFrame(profile_content, fg_color="transparent")
        stats_frame.pack(pady=15)
        
        posts_count = len(self.data_manager.get_user_posts(self.current_user))
        friends_count = len(user.friends)
        
        ctk.CTkLabel(stats_frame, text=f"{posts_count} Posts", font=Theme.FONT_BODY).pack(side="left", padx=15)
        ctk.CTkLabel(stats_frame, text=f"{friends_count} Friends", font=Theme.FONT_BODY).pack(side="left", padx=15)
        
        # Edit button
        edit_btn = ctk.CTkButton(
            profile_content,
            text="Edit Profile",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=self.show_edit_profile
        )
        edit_btn.pack(pady=10)
        
        # Tabs for Posts and Friends
        tab_frame = ctk.CTkFrame(self.main_content, fg_color="transparent")
        tab_frame.pack(fill="x", padx=20, pady=10)
        
        self.profile_tab = "posts"
        
        self.posts_tab_btn = ctk.CTkButton(
            tab_frame,
            text="📝 Posts",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.switch_profile_tab("posts")
        )
        self.posts_tab_btn.pack(side="left", padx=5)
        
        self.friends_tab_btn = ctk.CTkButton(
            tab_frame,
            text="👥 Friends",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.switch_profile_tab("friends")
        )
        self.friends_tab_btn.pack(side="left", padx=5)
        
        # Content area
        self.profile_content_area = ctk.CTkScrollableFrame(
            self.main_content,
            fg_color="transparent"
        )
        self.profile_content_area.pack(fill="both", expand=True, padx=20, pady=10)
        
        self.load_profile_content()
    
    def switch_profile_tab(self, tab):
        """Switch between profile tabs"""
        self.profile_tab = tab
        
        self.posts_tab_btn.configure(fg_color=Theme.BACKGROUND_LIGHT)
        self.friends_tab_btn.configure(fg_color=Theme.BACKGROUND_LIGHT)
        
        if tab == "posts":
            self.posts_tab_btn.configure(fg_color=Theme.PRIMARY)
        else:
            self.friends_tab_btn.configure(fg_color=Theme.PRIMARY)
        
        self.load_profile_content()
    
    def load_profile_content(self):
        """Load content for profile tab"""
        for widget in self.profile_content_area.winfo_children():
            widget.destroy()
        
        if self.profile_tab == "posts":
            self.load_user_posts()
        else:
            self.load_friends_list()
    
    def load_user_posts(self):
        """Load user's posts with sorting options"""
        # Sorting controls
        sort_frame = ctk.CTkFrame(self.profile_content_area, fg_color="transparent")
        sort_frame.pack(fill="x", pady=10)
        
        ctk.CTkLabel(sort_frame, text="Sort by:", font=Theme.FONT_BODY).pack(side="left", padx=10)
        
        self.post_sort = "newest"
        
        newest_btn = ctk.CTkButton(
            sort_frame,
            text="Newest",
            width=100,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.sort_user_posts("newest")
        )
        newest_btn.pack(side="left", padx=5)
        
        oldest_btn = ctk.CTkButton(
            sort_frame,
            text="Oldest",
            width=100,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.sort_user_posts("oldest")
        )
        oldest_btn.pack(side="left", padx=5)
        
        popular_btn = ctk.CTkButton(
            sort_frame,
            text="Popular",
            width=100,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.sort_user_posts("popular")
        )
        popular_btn.pack(side="left", padx=5)
        
        self.post_sort_buttons = {"newest": newest_btn, "oldest": oldest_btn, "popular": popular_btn}
        
        # Posts container
        posts_container = ctk.CTkFrame(self.profile_content_area, fg_color="transparent")
        posts_container.pack(fill="both", expand=True)
        
        posts = self.data_manager.get_user_posts(self.current_user)
        
        # Sort posts
        if self.post_sort == "newest":
            posts = SortAlgorithms.merge_sort(posts, key=lambda p: p.timestamp, reverse=True)
        elif self.post_sort == "oldest":
            posts = SortAlgorithms.merge_sort(posts, key=lambda p: p.timestamp, reverse=False)
        else:  # popular
            posts = SortAlgorithms.quick_sort(posts, key=lambda p: len(p.likes), reverse=True)
        
        if not posts:
            ctk.CTkLabel(
                posts_container,
                text="No posts yet",
                font=Theme.FONT_BODY,
                text_color=Theme.TEXT_SECONDARY
            ).pack(pady=50)
        else:
            for post in posts:
                card = PostCard(
                    posts_container,
                    post,
                    self.current_user,
                    self.data_manager,
                    on_update=self.load_profile_content
                )
                card.pack(fill="x", pady=10)
    
    def sort_user_posts(self, sort_type):
        """Change post sorting"""
        self.post_sort = sort_type
        
        # Update button colors
        for key, btn in self.post_sort_buttons.items():
            btn.configure(fg_color=Theme.PRIMARY if key == sort_type else Theme.BACKGROUND_LIGHT)
        
        self.load_profile_content()
    
    def load_friends_list(self):
        """Load friends list with search"""
        # Search and controls
        controls_frame = ctk.CTkFrame(self.profile_content_area, fg_color="transparent")
        controls_frame.pack(fill="x", pady=10)
        
        self.friends_search = ctk.CTkEntry(
            controls_frame,
            placeholder_text="Search friends...",
            width=250,
            height=35,
            corner_radius=Theme.BUTTON_CORNER_RADIUS
        )
        self.friends_search.pack(side="left", padx=5)
        self.friends_search.bind('<KeyRelease>', lambda e: self.filter_friends())
        
        find_friends_btn = ctk.CTkButton(
            controls_frame,
            text="Find New Friends",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=self.show_find_friends
        )
        find_friends_btn.pack(side="right", padx=5)
        
        # Sort buttons
        self.friends_sort = "alphabetical"
        
        alpha_btn = ctk.CTkButton(
            controls_frame,
            text="A-Z",
            width=80,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.sort_friends("alphabetical")
        )
        alpha_btn.pack(side="left", padx=5)
        
        recent_btn = ctk.CTkButton(
            controls_frame,
            text="Recent",
            width=80,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.sort_friends("recent")
        )
        recent_btn.pack(side="left", padx=5)
        
        self.friends_sort_buttons = {"alphabetical": alpha_btn, "recent": recent_btn}
        
        # Friends container
        self.friends_container = ctk.CTkFrame(self.profile_content_area, fg_color="transparent")
        self.friends_container.pack(fill="both", expand=True)
        
        self.display_friends()
    
    def filter_friends(self):
        """Filter friends by search query"""
        self.display_friends()
    
    def sort_friends(self, sort_type):
        """Change friends sorting"""
        self.friends_sort = sort_type
        
        # Update button colors
        for key, btn in self.friends_sort_buttons.items():
            btn.configure(fg_color=Theme.PRIMARY if key == sort_type else Theme.BACKGROUND_LIGHT)
        
        self.display_friends()
    
    def display_friends(self):
        """Display friends list"""
        for widget in self.friends_container.winfo_children():
            widget.destroy()
        
        friends = self.data_manager.get_friends(self.current_user)
        
        # Apply search filter
        search_query = self.friends_search.get().strip().lower()
        if search_query:
            friends = [f for f in friends if search_query in f.username.lower() or search_query in f.name.lower()]
        
        # Sort friends
        if self.friends_sort == "alphabetical":
            friends = SortAlgorithms.insertion_sort(friends, key=lambda f: f.name.lower())
        else:  # recent
            # Sort by when they became friends (reverse order in friends list)
            friends = friends[::-1]
        
        if not friends:
            ctk.CTkLabel(
                self.friends_container,
                text="No friends found",
                font=Theme.FONT_BODY,
                text_color=Theme.TEXT_SECONDARY
            ).pack(pady=50)
        else:
            for friend in friends:
                self.create_friend_card(self.friends_container, friend)
    
    def create_friend_card(self, parent, friend):
        """Create a friend card widget"""
        card = ctk.CTkFrame(parent, fg_color=Theme.CARD_BG, corner_radius=Theme.CORNER_RADIUS)
        card.pack(fill="x", pady=5)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="x", padx=15, pady=15)
        
        # Profile pic
        ctk.CTkLabel(content, text="👤", font=("Segoe UI", 30)).pack(side="left", padx=10)
        
        # Info
        info_frame = ctk.CTkFrame(content, fg_color="transparent")
        info_frame.pack(side="left", fill="x", expand=True)
        
        ctk.CTkLabel(info_frame, text=friend.name, font=Theme.FONT_SUBHEADING, anchor="w").pack(anchor="w")
        ctk.CTkLabel(info_frame, text=f"@{friend.username}", font=Theme.FONT_SMALL, text_color=Theme.TEXT_SECONDARY, anchor="w").pack(anchor="w")
        
        # View profile button
        view_btn = ctk.CTkButton(
            content,
            text="View Profile",
            width=100,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=lambda: self.view_friend_profile(friend.username)
        )
        view_btn.pack(side="right", padx=5)
    
    def view_friend_profile(self, username):
        """View a friend's profile"""
        # Clear main content
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        user = self.data_manager.get_user(username)
        if not user:
            messagebox.showerror("Error", "User not found")
            self.show_profile()
            return
        
        # Profile header
        header = ctk.CTkFrame(self.main_content, fg_color=Theme.CARD_BG, corner_radius=Theme.CORNER_RADIUS)
        header.pack(fill="x", padx=20, pady=20)
        
        profile_content = ctk.CTkFrame(header, fg_color="transparent")
        profile_content.pack(padx=30, pady=30)
        
        # Profile picture
        ctk.CTkLabel(profile_content, text="👤", font=("Segoe UI", 60)).pack()
        
        # User info
        ctk.CTkLabel(profile_content, text=user.name, font=Theme.FONT_HEADING).pack()
        ctk.CTkLabel(profile_content, text=f"@{user.username}", font=Theme.FONT_BODY, text_color=Theme.TEXT_SECONDARY).pack()
        
        if user.bio:
            ctk.CTkLabel(profile_content, text=user.bio, font=Theme.FONT_SMALL, wraplength=400).pack(pady=10)
        
        # Stats
        stats_frame = ctk.CTkFrame(profile_content, fg_color="transparent")
        stats_frame.pack(pady=15)
        
        posts_count = len(self.data_manager.get_user_posts(username))
        friends_count = len(user.friends)
        
        ctk.CTkLabel(stats_frame, text=f"{posts_count} Posts", font=Theme.FONT_BODY).pack(side="left", padx=15)
        ctk.CTkLabel(stats_frame, text=f"{friends_count} Friends", font=Theme.FONT_BODY).pack(side="left", padx=15)
        
        # Back button
        back_btn = ctk.CTkButton(
            profile_content,
            text="← Back to My Profile",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=self.show_profile
        )
        back_btn.pack(pady=10)
        
        # Show user's posts
        ctk.CTkLabel(
            self.main_content,
            text=f"{user.name}'s Posts",
            font=Theme.FONT_HEADING
        ).pack(padx=20, pady=(10, 5))
        
        # Posts container
        posts_container = ctk.CTkScrollableFrame(
            self.main_content,
            fg_color="transparent"
        )
        posts_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        posts = self.data_manager.get_user_posts(username)
        posts = SortAlgorithms.merge_sort(posts, key=lambda p: p.timestamp, reverse=True)
        
        if not posts:
            ctk.CTkLabel(
                posts_container,
                text="No posts yet",
                font=Theme.FONT_BODY,
                text_color=Theme.TEXT_SECONDARY
            ).pack(pady=50)
        else:
            for post in posts:
                card = PostCard(
                    posts_container,
                    post,
                    self.current_user,
                    self.data_manager,
                    on_update=lambda: self.view_friend_profile(username)
                )
                card.pack(fill="x", pady=10)
    
    def show_find_friends(self):
        """Show find friends dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Find Friends")
        dialog.geometry("500x600")
        dialog.transient(self)
        dialog.grab_set()
        
        # Title
        ctk.CTkLabel(dialog, text="Find New Friends", font=Theme.FONT_HEADING).pack(pady=20)
        
        # Search
        search_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        search_frame.pack(fill="x", padx=20, pady=10)
        
        search_entry = ctk.CTkEntry(
            search_frame,
            placeholder_text="Search users...",
            height=35,
            corner_radius=Theme.BUTTON_CORNER_RADIUS
        )
        search_entry.pack(fill="x")
        
        # Results container
        results_container = ctk.CTkScrollableFrame(dialog, fg_color="transparent")
        results_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        def search_users():
            """Search for users"""
            for widget in results_container.winfo_children():
                widget.destroy()
            
            query = search_entry.get().strip()
            if not query:
                return
            
            results = self.data_manager.search_users(query)
            current_user_obj = self.data_manager.get_user(self.current_user)
            
            for user in results:
                if user.username == self.current_user:
                    continue
                
                user_card = ctk.CTkFrame(results_container, fg_color=Theme.CARD_BG, corner_radius=Theme.CORNER_RADIUS)
                user_card.pack(fill="x", pady=5)
                
                content = ctk.CTkFrame(user_card, fg_color="transparent")
                content.pack(fill="x", padx=15, pady=15)
                
                # Profile
                ctk.CTkLabel(content, text="👤", font=("Segoe UI", 30)).pack(side="left", padx=10)
                
                # Info
                info = ctk.CTkFrame(content, fg_color="transparent")
                info.pack(side="left", fill="x", expand=True)
                
                ctk.CTkLabel(info, text=user.name, font=Theme.FONT_SUBHEADING, anchor="w").pack(anchor="w")
                ctk.CTkLabel(info, text=f"@{user.username}", font=Theme.FONT_SMALL, text_color=Theme.TEXT_SECONDARY, anchor="w").pack(anchor="w")
                
                # Action button
                if user.username in current_user_obj.friends:
                    ctk.CTkLabel(content, text="✓ Friends", font=Theme.FONT_SMALL, text_color=Theme.PRIMARY).pack(side="right")
                elif user.username in current_user_obj.friend_requests_sent:
                    ctk.CTkLabel(content, text="Pending", font=Theme.FONT_SMALL, text_color=Theme.TEXT_SECONDARY).pack(side="right")
                else:
                    add_btn = ctk.CTkButton(
                        content,
                        text="Add Friend",
                        width=100,
                        corner_radius=Theme.BUTTON_CORNER_RADIUS,
                        fg_color=Theme.PRIMARY,
                        hover_color=Theme.BUTTON_HOVER,
                        command=lambda u=user.username: self.send_friend_request(u, search_users)
                    )
                    add_btn.pack(side="right")
        
        search_entry.bind('<KeyRelease>', lambda e: search_users())
        
        # Close button
        close_btn = ctk.CTkButton(
            dialog,
            text="Close",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=dialog.destroy
        )
        close_btn.pack(pady=20)
    
    def send_friend_request(self, to_username, refresh_callback=None):
        """Send friend request"""
        success, message = self.data_manager.send_friend_request(self.current_user, to_username)
        if success:
            messagebox.showinfo("Success", message)
            if refresh_callback:
                refresh_callback()
        else:
            messagebox.showerror("Error", message)
    
    def show_edit_profile(self):
        """Show edit profile dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Edit Profile")
        dialog.geometry("400x500")
        dialog.transient(self)
        dialog.grab_set()
        
        user = self.data_manager.get_user(self.current_user)
        
        ctk.CTkLabel(dialog, text="Edit Profile", font=Theme.FONT_HEADING).pack(pady=20)
        
        # Form
        name_entry = self.create_entry(dialog, "Name")
        name_entry.insert(0, user.name)
        
        bio_entry = self.create_entry(dialog, "Bio")
        bio_entry.insert(0, user.bio)
        
        dob_entry = self.create_entry(dialog, "Date of Birth")
        dob_entry.insert(0, user.dob)
        
        def save_changes():
            self.data_manager.update_user(
                self.current_user,
                name=name_entry.get().strip(),
                bio=bio_entry.get().strip(),
                dob=dob_entry.get().strip()
            )
            messagebox.showinfo("Success", "Profile updated!")
            dialog.destroy()
            self.show_profile()
        
        save_btn = ctk.CTkButton(
            dialog,
            text="Save Changes",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=save_changes
        )
        save_btn.pack(pady=15)
        
        cancel_btn = ctk.CTkButton(
            dialog,
            text="Cancel",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=dialog.destroy
        )
        cancel_btn.pack()
    
    def show_notifications(self):
        """Show notifications"""
        for widget in self.main_content.winfo_children():
            widget.destroy()
        
        # Header
        header = ctk.CTkFrame(self.main_content, fg_color=Theme.BACKGROUND_LIGHT, height=80)
        header.pack(fill="x", padx=20, pady=20)
        header.pack_propagate(False)
        
        ctk.CTkLabel(header, text="Notifications", font=Theme.FONT_HEADING).pack(side="left", padx=20)
        
        mark_read_btn = ctk.CTkButton(
            header,
            text="Mark All Read",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=self.mark_all_read
        )
        mark_read_btn.pack(side="right", padx=20)
        
        # Notifications container
        notif_container = ctk.CTkScrollableFrame(self.main_content, fg_color="transparent")
        notif_container.pack(fill="both", expand=True, padx=20, pady=10)
        
        notifications = self.data_manager.get_notifications(self.current_user)
        
        if not notifications:
            ctk.CTkLabel(
                notif_container,
                text="No notifications",
                font=Theme.FONT_BODY,
                text_color=Theme.TEXT_SECONDARY
            ).pack(pady=50)
        else:
            for notif in reversed(notifications):  # Most recent first
                self.create_notification_card(notif_container, notif)
    
    def create_notification_card(self, parent, notif):
        """Create notification card"""
        card = ctk.CTkFrame(
            parent,
            fg_color=Theme.CARD_BG if notif.read else Theme.PRIMARY,
            corner_radius=Theme.CORNER_RADIUS
        )
        card.pack(fill="x", pady=5)
        
        content = ctk.CTkFrame(card, fg_color="transparent")
        content.pack(fill="x", padx=15, pady=15)
        
        # Icon based on type
        icons = {
            Notification.TYPE_LIKE: "❤️",
            Notification.TYPE_COMMENT: "💬",
            Notification.TYPE_FRIEND_REQUEST: "👥",
            Notification.TYPE_FRIEND_ACCEPTED: "✓"
        }
        icon = icons.get(notif.type, "🔔")
        
        ctk.CTkLabel(content, text=icon, font=("Segoe UI", 24)).pack(side="left", padx=10)
        
        # Message
        info_frame = ctk.CTkFrame(content, fg_color="transparent")
        info_frame.pack(side="left", fill="x", expand=True)
        
        ctk.CTkLabel(
            info_frame,
            text=notif.message,
            font=Theme.FONT_BODY,
            anchor="w",
            wraplength=400
        ).pack(anchor="w")
        
        time_str = datetime.fromisoformat(notif.timestamp).strftime("%b %d, %I:%M %p")
        ctk.CTkLabel(
            info_frame,
            text=time_str,
            font=Theme.FONT_SMALL,
            text_color=Theme.TEXT_SECONDARY,
            anchor="w"
        ).pack(anchor="w")
        
        # Accept button for friend requests (check if still pending)
        if notif.type == Notification.TYPE_FRIEND_REQUEST:
            user = self.data_manager.get_user(self.current_user)
            if notif.from_user in user.friend_requests_received:
                accept_btn = ctk.CTkButton(
                    content,
                    text="Accept",
                    width=80,
                    corner_radius=Theme.BUTTON_CORNER_RADIUS,
                    fg_color="#4CAF50",
                    hover_color="#45a049",
                    command=lambda: self.accept_friend_request(notif.from_user)
                )
                accept_btn.pack(side="right", padx=5)
            elif notif.from_user in user.friends:
                ctk.CTkLabel(
                    content,
                    text="✓ Friends",
                    font=Theme.FONT_SMALL,
                    text_color="#4CAF50"
                ).pack(side="right", padx=5)
    
    def accept_friend_request(self, from_username):
        """Accept friend request"""
        if self.data_manager.accept_friend_request(self.current_user, from_username):
            messagebox.showinfo("Success", "Friend request accepted!")
            self.show_notifications()
    
    def mark_all_read(self):
        """Mark all notifications as read"""
        self.data_manager.mark_notifications_read(self.current_user)
        self.show_notifications()
    
    def show_create_post(self):
        """Show create post dialog"""
        dialog = ctk.CTkToplevel(self)
        dialog.title("Create Post")
        dialog.geometry("500x400")
        dialog.transient(self)
        dialog.grab_set()
        
        ctk.CTkLabel(dialog, text="Create New Post", font=Theme.FONT_HEADING).pack(pady=20)
        
        # Text input
        ctk.CTkLabel(dialog, text="Post Content *", font=Theme.FONT_BODY, anchor="w").pack(anchor="w", padx=30)
        text_input = ctk.CTkTextbox(
            dialog,
            height=150,
            corner_radius=Theme.BUTTON_CORNER_RADIUS
        )
        text_input.pack(padx=30, pady=10, fill="both", expand=True)
        
        # Media (optional)
        media_frame = ctk.CTkFrame(dialog, fg_color="transparent")
        media_frame.pack(fill="x", padx=30, pady=10)
        
        media_label = ctk.CTkLabel(media_frame, text="No media selected", font=Theme.FONT_SMALL, text_color=Theme.TEXT_SECONDARY)
        media_label.pack(side="left")
        
        self.selected_media = ""
        
        def select_media():
            filepath = filedialog.askopenfilename(
                title="Select Media",
                filetypes=[("Image/Video", "*.jpg *.jpeg *.png *.gif *.mp4 *.avi")]
            )
            if filepath:
                self.selected_media = filepath
                media_label.configure(text=os.path.basename(filepath))
        
        media_btn = ctk.CTkButton(
            media_frame,
            text="Add Media",
            width=100,
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=select_media
        )
        media_btn.pack(side="right")
        
        # Buttons
        def create_post():
            text = text_input.get("1.0", "end-1c").strip()
            if not text:
                messagebox.showerror("Error", "Post content is required!")
                return
            
            post, message = self.data_manager.create_post(self.current_user, text, self.selected_media)
            if post:
                messagebox.showinfo("Success", message)
                dialog.destroy()
                self.show_home_feed()
            else:
                messagebox.showerror("Error", message)
        
        create_btn = ctk.CTkButton(
            dialog,
            text="Create Post",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.PRIMARY,
            hover_color=Theme.BUTTON_HOVER,
            command=create_post
        )
        create_btn.pack(pady=10)
        
        cancel_btn = ctk.CTkButton(
            dialog,
            text="Cancel",
            corner_radius=Theme.BUTTON_CORNER_RADIUS,
            fg_color=Theme.BACKGROUND_LIGHT,
            hover_color=Theme.BUTTON_HOVER,
            command=dialog.destroy
        )
        cancel_btn.pack()
    
    def undo_action(self):
        """Undo last action"""
        success, message = self.data_manager.undo_last_action()
        if success:
            messagebox.showinfo("Success", message)
            self.show_home_feed()
        else:
            messagebox.showinfo("Info", message)
    
    def logout(self):
        """Logout user"""
        self.current_user = None
        self.show_login_screen()

# ===================== MAIN ENTRY POINT =====================

if __name__ == "__main__":
    app = SocialMediaApp()
    app.mainloop() 