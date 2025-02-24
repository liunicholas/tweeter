import React, { useState, useEffect, useCallback, useRef } from 'react';
import { View, Text, TextInput, Button } from 'react-native';

interface Post {
  id: string;
  content: string;
  likes: number;
  timestamp: Date;
}

export default function PostScreen() {
  // useState Hook Examples
  // useState returns an array with two elements:
  // 1. The current state value
  // 2. A function to update that value
  const [posts, setPosts] = useState<Post[]>([]); // Managing an array of posts
  const [newPostContent, setNewPostContent] = useState(''); // Managing form input
  const [isPosting, setIsPosting] = useState(false); // Managing loading state

  // useRef Hook Examples
  // useRef returns a mutable object that persists across re-renders
  // Unlike state variables, changing ref values doesn't trigger re-renders
  const isMounted = useRef(false); // Used to track component mount status
  const postViewCount = useRef(0); // Tracks views without causing re-renders

  // useEffect Hook with empty dependency array ([])
  // This effect runs once when component mounts and cleanup runs on unmount
  useEffect(() => {
    isMounted.current = true;
    console.log('PostScreen mounted');
    
    // Cleanup function (optional)
    // Runs before component unmounts or before next effect execution
    return () => {
      isMounted.current = false;
      console.log('PostScreen unmounted');
    };
  }, []);

  // useEffect Hook with dependencies
  // This effect runs whenever the 'posts' array changes
  useEffect(() => {
    postViewCount.current += 1;
    console.log(`Post screen viewed ${postViewCount.current} times`);
  }, [posts]);

  // useCallback Hook
  // Memoizes functions to prevent unnecessary re-renders in child components
  // Only recreates the function if dependencies change
  const createPost = useCallback(() => {
    if (!newPostContent.trim()) return;

    setIsPosting(true); // Update loading state
    
    // Simulate API call with setTimeout
    // In a real app, this would be an actual API request
    setTimeout(() => {
      const newPost: Post = {
        id: Date.now().toString(),
        content: newPostContent,
        likes: 0,
        timestamp: new Date()
      };

      // Functional update pattern ensures we always have the latest state
      setPosts(prevPosts => [...prevPosts, newPost]);
      setNewPostContent('');
      setIsPosting(false);
    }, 1000);
  }, [newPostContent]); // Function recreates if newPostContent changes

  // useCallback for post interactions
  // These functions are memoized to prevent unnecessary re-renders
  const likePost = useCallback((postId: string) => {
    // Functional update pattern for modifying specific items in an array
    setPosts(prevPosts =>
      prevPosts.map(post =>
        post.id === postId
          ? { ...post, likes: post.likes + 1 }
          : post
      )
    );
  }, []);

  const deletePost = useCallback((postId: string) => {
    // Functional update pattern for filtering arrays
    setPosts(prevPosts => prevPosts.filter(post => post.id !== postId));
  }, []);

  return (
    <View>
      <TextInput
        value={newPostContent}
        onChangeText={setNewPostContent}
        placeholder="Write your post..."
      />
      <Button
        title={isPosting ? "Posting..." : "Create Post"}
        onPress={createPost}
        disabled={isPosting || !newPostContent.trim()}
      />

      {posts.map(post => (
        <View key={post.id}>
          <Text>{post.content}</Text>
          <Text>Likes: {post.likes}</Text>
          <Button title="Like" onPress={() => likePost(post.id)} />
          <Button title="Delete" onPress={() => deletePost(post.id)} />
        </View>
      ))}
    </View>
  );
}
