import React from "react";
import { View, TextInput, Button } from "react-native";

// Define props interface
interface PostInputProps {
  value: string;
  onChangeText: (text: string) => void;
  onSubmit: () => void;
  isPosting: boolean;
}

// PostInput handles the creation of new posts
// It contains the input field and submit button
export const PostInput: React.FC<PostInputProps> = ({
  value,
  onChangeText,
  onSubmit,
  isPosting,
}) => {
  return (
    <View>
      {/* Input field for post content */}
      <TextInput
        value={value}
        onChangeText={onChangeText}
        placeholder="Write your post..."
        // Disable input while posting
        editable={!isPosting}
      />

      {/* Submit button with loading state */}
      <Button
        title={isPosting ? "Posting..." : "Create Post"}
        onPress={onSubmit}
        // Disable button when posting or when input is empty
        disabled={isPosting || !value.trim()}
      />
    </View>
  );
};
