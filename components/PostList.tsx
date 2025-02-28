import React from "react";
import { View, Text, ScrollView, StyleSheet } from "react-native";
import { PostCard } from "./PostCard";

// Define the Post type
interface Post {
  id: string;
  content: string;
  likes: number;
  timestamp: Date;
  imageUri?: string;
}

// Define props interface
interface PostListProps {
  posts: Post[];
  onLikePost: (postId: string) => void;
  onDeletePost: (postId: string) => void;
}

// PostList renders the list of posts using the PostCard component
export const PostList: React.FC<PostListProps> = ({
  posts,
  onLikePost,
  onDeletePost,
}) => {
  // If there are no posts, show a message
  if (posts.length === 0) {
    return (
      <View style={styles.emptyContainer}>
        <Text style={styles.emptyText}>
          No posts yet. Be the first to post!
        </Text>
      </View>
    );
  }

  // Render the list of posts
  return (
    <ScrollView style={styles.container}>
      {posts.map((post) => (
        <PostCard
          key={post.id}
          content={post.content}
          likes={post.likes}
          imageUri={post.imageUri}
          onLike={() => onLikePost(post.id)}
          onDelete={() => onDeletePost(post.id)}
        />
      ))}
    </ScrollView>
  );
};

// Styles for the PostList component
const styles = StyleSheet.create({
  // Main container for the list
  container: {
    flex: 1,
  },
  // Styling for empty state container
  emptyContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
    padding: 20,
  },
  // Styling for empty state text
  emptyText: {
    fontSize: 16,
    color: "#666",
    textAlign: "center",
  },
});
