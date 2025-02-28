import React, { useState, useEffect, useCallback, useRef } from "react";
import { View, StyleSheet } from "react-native";
// Import our new components
import { PostInput } from "../../components/PostInput";
import { PostList } from "../../components/PostList";

interface Post {
  id: string;
  content: string;
}

export default function PostScreen() {
  // useState Hook Examples
  // useState returns an array with two elements:
  // 1. The current state value
  // 2. A function to update that value
  const [posts, setPosts] = useState<Post[]>([]); // Managing an array of posts
  const [newPostContent, setNewPostContent] = useState(""); // Managing form input
  const [isPosting, setIsPosting] = useState(false); // Managing loading state

  // useRef Hook Examples
  // useRef returns a mutable object that persists across re-renders
  // Unlike state variables, changing ref values doesn't trigger re-renders
  const isMounted = useRef(false); // Used to track component mount status

  // useEffect Hook with empty dependency array ([])
  // This effect runs once when component mounts and cleanup runs on unmount
  useEffect(() => {
    isMounted.current = true;
    console.log("PostScreen mounted");

    // Cleanup function (optional)
    // Runs before component unmounts or before next effect execution
    return () => {
      isMounted.current = false;
      console.log("PostScreen unmounted");
    };
  }, []);

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
      };

      // Functional update pattern ensures we always have the latest state
      setPosts((prevPosts) => [...prevPosts, newPost]);
      setNewPostContent("");
      setIsPosting(false);
    }, 1000);
  }, [newPostContent]); // Function recreates if newPostContent changes

  return (
    <View style={styles.container}>
      <PostInput
        value={newPostContent}
        onChangeText={setNewPostContent}
        onSubmit={createPost}
        isPosting={isPosting}
      />

      <PostList posts={posts} />
    </View>
  );
}

// Styles for the PostScreen component
const styles = StyleSheet.create({
  // Container uses flex layout for proper spacing
  container: {
    flex: 1,
    padding: 16,
    backgroundColor: "#f5f5f5",
  },
});
