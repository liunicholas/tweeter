import React from "react";
import { View, Text } from "react-native";
import { PostCard } from "./PostCard";

// Define the Post type
interface Post {
  id: string;
  content: string;
}

// Define props interface
interface PostListProps {
  posts: Post[];
}

// PostList renders the list of posts using the PostCard component
export const PostList: React.FC<PostListProps> = ({ posts }) => {
  // If there are no posts, show a message
  if (posts.length === 0) {
    return (
      <View>
        <Text>No posts yet. Be the first to post!</Text>
      </View>
    );
  }

  // Render the list of posts
  return (
    <View>
      {posts.map((post) => (
        <PostCard key={post.id} content={post.content} />
      ))}
    </View>
  );
};
