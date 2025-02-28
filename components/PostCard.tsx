import React from "react";
import { View, Text, Button } from "react-native";

// Define the props interface to ensure type safety
interface PostCardProps {
  content: string;
}

// PostCard is a presentational component that displays a single post
// It receives data and callbacks as props from its parent component
export const PostCard: React.FC<PostCardProps> = ({ content }) => {
  return (
    <View>
      {/* Display the post content */}
      <Text>{content}</Text>
    </View>
  );
};
