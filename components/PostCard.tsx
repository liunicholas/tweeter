import React from "react";
import { View, Text, Button, StyleSheet } from "react-native";

// Define the props interface to ensure type safety
interface PostCardProps {
  content: string;
}

// PostCard is a presentational component that displays a single post
// It receives data and callbacks as props from its parent component
export const PostCard: React.FC<PostCardProps> = ({ content }) => {
  return (
    <View style={styles.card}>
      {/* Display the post content */}
      <Text style={styles.content}>{content}</Text>
    </View>
  );
};

// Styles for the PostCard component
const styles = StyleSheet.create({
  // Main card container
  card: {
    backgroundColor: "#ffffff",
    borderRadius: 8,
    padding: 16,
    marginVertical: 8,
    // iOS shadow
    shadowColor: "#000",
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.1,
    shadowRadius: 4,
    // Android shadow
    elevation: 3,
  },
  // Post content text
  content: {
    fontSize: 16,
    marginBottom: 12,
    lineHeight: 24,
  },
});
